import pandas as pd
import numpy as np
from sklearn import preprocessing # Use for normalization for classification data

# Authors:
# Jacob Clostio and Nick Leopold

def NN(train, numHLayers, num_nodes, arrayWeightMatrix, arrayBiasWeights, data_type):
  
  
    learningRate = 0.000625
    if data_type == 'regression':
      train = train/np.linalg.norm(train) # normalize data for regression
    
    training = train.iloc[: , :-1] # separate class column from dataframe
    training_classes = train.iloc[: , -1]

    if data_type == 'classification':
      train = preprocessing.normalize(train)
    training_classes = training_classes.values.tolist()
    training = training.values.tolist()
   
    classes = np.unique(training_classes) # get list of possible classes (possible outputs)

    arrayOfNodeValues = [] # This needs to be incremented each time a hidden layer gets new node values (and output vals)
    # need a case for when there are 0 hidden layers
    if len(arrayWeightMatrix) < 2: # initializes random weight matrix if the weight matrix does not exist yet
      if(numHLayers == 0):
        arrayBiasWeights.append(np.zeros((len(classes), 1)))
        arrayWeightMatrix.append(np.random.uniform(-0.5,0.5, (len(classes), len(training[0])))) 
      else:
        for i in range(numHLayers):
          arrayBiasWeights.append(np.zeros((num_nodes[i], 1)))
          if(i == 0):
            arrayWeightMatrix.append(np.random.uniform(-0.5,0.5, (num_nodes[i], len(training[0])))) # initialize random weights matrix
          else:
            arrayWeightMatrix.append(np.random.uniform(-0.5,0.5, (num_nodes[i], num_nodes[i-1])))
      if data_type == 'classification' and numHLayers != 0:
        arrayWeightMatrix.append(np.random.uniform(-0.5,0.5, (len(classes), num_nodes[-1]))) # from last hidden to output.
        arrayBiasWeights.append(np.zeros((len(classes), 1)))
      elif numHLayers != 0:
        arrayWeightMatrix.append(np.random.uniform(-0.5,0.5, (1, num_nodes[-1])))
        arrayBiasWeights.append(np.zeros((1, 1)))
    prev_change = [0]*(numHLayers+1)

    numCorrect = 0 # init vars
    total = 0
    accuracy = 0
    mse = [1]
    epochs = 0
    totalmse=0
    while(accuracy < .8 and mse[0] > 0.001): # performs another epoch until one of these conditions is satisfied
      print("Accuracy: " + str(accuracy))
      epochs += 1
      
      if data_type == 'regression' and mse[0] != 1:
        print(mse[0])
        mse = (np.sum(arrayOfNodeValues[-1])-label)**2/len(training[0])
      if(total != 0):
       # oldAccuracy = accuracy
        accuracy = numCorrect/total
      total = 0
      numCorrect = 0
      
      for i in range(len(training)): # iterate through rows of trainging data
        # Need to insert node values into the arrayOfNodeValues data structure
        if data_type == 'classification':
          label = [0]*len(classes) # initialize label array
          for j in range(len(classes)):
            if classes[j] == training_classes[i]: # set label array value to 1 if classes match
              label[j] = 1
            else:
              label[j] = 0 # set label array values to 0 if classes do not match
          label = np.asarray(label)
          label.shape += (1,)
        else:
          label = training_classes[i]
          label = np.asarray(label)
          label.shape += (1,)
          label = label.astype(float)
        arrayOfNodeValues = []
 
        arrayOfNodeValues.append(np.array(training[i]))
        arrayOfNodeValues[0].shape += (1,)
        for k in range(numHLayers+1):
          hiddenNodeVal = arrayBiasWeights[k] + (arrayWeightMatrix[k] @ arrayOfNodeValues[k])
          if data_type == 'classification':
            normalizedHiddenNodeVal = 1 / (1 + np.exp(-hiddenNodeVal)) # softmax function for classification
          else:
            normalizedHiddenNodeVal = hiddenNodeVal # linear activation for regression
            
              
          arrayOfNodeValues.append(normalizedHiddenNodeVal)
        
        if data_type == 'classification': # collect data for accuracy measurement
          if(np.argmax(arrayOfNodeValues[-1])+1 == np.argmax(label)+1):
            numCorrect += 1
          total += 1

        else: # calculate mean squared error for regression
          mse = (np.sum(arrayOfNodeValues[-1])-label)**2/len(training[i])
          totalmse += mse
          
        arrayWeightMatrix, arrayBiasWeights, prev_change = backProp(arrayOfNodeValues, label, arrayWeightMatrix, arrayBiasWeights, learningRate, prev_change, 0.5, momentum=True) # decimal number is the momentum variable (0-1)
    if data_type == 'regression':
      print("Training MSE: " + str(totalmse/(len(train)*epochs)))    
    else:
      print("Training Accuracy: " + str(accuracy))
    print("Number of Epochs until convergence: " + str(epochs))
    return arrayWeightMatrix, arrayBiasWeights
  
      # input = np.transpose(training[:][i])
      # # NOTE: changed w_mat to arrayWeightMatrix[i] Not sure if this would be equiv
      # (np.matmul(arrayWeightMatrix[i],input)) # multiply training row by weight matrix

# Where arrayOfNodeValues is an array of all the node values
# labelArray is the array of the class label ex. [0, 1, 0, 0]
# arrayWeightMatrix is an array of weight matrices (the first entry being the input -> first hidden layer, second being hidden layer 1 to hidden layer 2, ..., last hidden layer n to output)
# arrayBiasWeights being an array of the bias nodes (same order as arrayWeightMatrix)
# learning rate being the learning rate

def backProp(arrayOfNodeValues, labelArray, arrayWeightMatrix, arrayBiasWeights, learningRate, prev_change, m, momentum):


  if(len(arrayOfNodeValues) == 2): # For the case of 0 hidden layers.
    if type(prev_change[0] == int):
      delta = arrayOfNodeValues[-1] - labelArray
    if momentum == True:
      delta = arrayOfNodeValues[-1] - labelArray + m*prev_change[-1]
    else:
      delta = arrayOfNodeValues[-1] - labelArray
    arrayWeightMatrix[0]+= -learningRate * delta @ np.transpose(arrayOfNodeValues[0])
    arrayBiasWeights[0] += -learningRate * delta
    prev_change = delta
    return arrayWeightMatrix, arrayBiasWeights, prev_change 


  if type(prev_change[0]) == int: # check if this is the first change. type will change to array after update
    delta =  arrayOfNodeValues[-1] - labelArray 
  else:
    if momentum == True:
      delta =  arrayOfNodeValues[-1] - labelArray + m*prev_change[-1]# [-1] the output layer, m is the momentum parameter (0-1)
    else:
      delta =  arrayOfNodeValues[-1] - labelArray # if no momentum, this will be the delta update

  prev_change[-1] = delta
  for i in range(len(arrayWeightMatrix)): # iterate through all of the weight matrices (and bias weights)
    if(i == 0):
      arrayWeightMatrix[-1] += -learningRate * delta @ np.transpose(arrayOfNodeValues[-2])
      arrayBiasWeights[-1] += -learningRate * delta
    else:
      
      # arrayWeightMatrix[len(arrayWeightMatrix) - len(arrayWeightMatrix)+i] gives the last weight since we are going back from the output
      # arrayOfNodeValues[len(arrayOfNodeValues) - len(arrayOfNodeValues)+i+1] +1 because we want to ignore the output layer
      # also note that I will be 1 when it gets here (cause of if(i==0)) part, which is why Im adding 1 to the thing that will subtract.
      if type(prev_change[-i-1]) == int: # will change to array after update
        delta = np.transpose(arrayWeightMatrix[-i]) @ delta * ((arrayOfNodeValues[-i-1]) * (1-(arrayOfNodeValues[-i-1]))) # case where there are no previous weight changes yet
      else:
        if momentum == True:
          delta = np.transpose(arrayWeightMatrix[-i]) @ delta * ((arrayOfNodeValues[-i-1]) * (1-(arrayOfNodeValues[-i-1]))) + m*prev_change[-1-i] # with momentum 
        else:
          delta = np.transpose(arrayWeightMatrix[-i]) @ delta * ((arrayOfNodeValues[-i-1]) * (1-(arrayOfNodeValues[-i-1]))) # without momentum

      arrayWeightMatrix[ - 1 - i] += -learningRate * delta @ np.transpose(arrayOfNodeValues[len(arrayOfNodeValues) - i-2]) # change weight matrix
      arrayBiasWeights[-i-1] += -learningRate * delta
      #arrayOfNodeValues[len(arrayOfNodeValues) -1 -i] = delta
      prev_change[-i-1] = delta # save weight change for next change with momentum

  return arrayWeightMatrix, arrayBiasWeights, prev_change
  
def testNN(test, numHLayers, arrayWeightMatrix, arrayBiasWeights, data_type):

  totalmse = 0


  if data_type == 'regression':
      test = test/np.linalg.norm(test) # normalize data for regression
    
  #test = test/np.linalg.norm(test) # normalize data
  testing = test.iloc[: , :-1] # separate class from test data
  test_classes = test.iloc[:, -1]

  if data_type == 'classification':
    test = preprocessing.normalize(test)
  testing = testing.values.tolist() # turn dataframes into lists
  test_classes = test_classes.values.tolist()

  test_outputs = np.unique(test_classes)
  total = 0
  numCorrect = 0

  for i in range(len(testing)): # iterate through rows of trainging data
      # Need to insert node values into the arrayOfNodeValues data structure
    if data_type == 'classification':
      label = [0]*len(test_outputs) # initialize label array
      for j in range(len(test_outputs)):
        if test_outputs[j] == test_classes[i]: # set label array value to 1 if classes match
          label[j] = 1
        else:
          label[j] = 0 # set label array values to 0 if classes do not match
      label = np.asarray(label)
      label.shape += (1,)
    else:
          label = test_classes[i]
          label = np.asarray(label)
          label.shape += (1,)
          label = label.astype(float)
        
    arrayOfNodeValues = []

    arrayOfNodeValues.append(np.array(testing[i]))
    arrayOfNodeValues[0].shape += (1,)

    for k in range(numHLayers+1):
      hiddenNodeVal = arrayBiasWeights[k] + (arrayWeightMatrix[k] @ arrayOfNodeValues[k])
      if data_type == 'classification':
        normalizedHiddenNodeVal = 1 / (1 + np.exp(-hiddenNodeVal)) # softmax function for classification
      else:
        if k<numHLayers:
          normalizedHiddenNodeVal = hiddenNodeVal # linear activation for regression
        elif k == numHLayers:
          normalizedHiddenNodeVal = hiddenNodeVal
      arrayOfNodeValues.append(normalizedHiddenNodeVal)
    if data_type == 'classification':
      if(np.argmax(arrayOfNodeValues[-1])+1 == np.argmax(label)+1):
        numCorrect += 1
      total += 1
      
    else: 
      mse = (np.sum(arrayOfNodeValues[-1])-label)**2/len(testing[i])
      totalmse += mse
  if data_type == 'regression':
    print("Test MSE: " + str(totalmse/len(test)))
  else:
    print("Test Accuracy: " + str(numCorrect/total))
  print("--------------------------------------------------")
  return numCorrect, total

def kfold(data):
    data = data.sample(frac=1)          # would shuffle all rows in df
    foldLen = int(len(data) / 10)       # int rounds down
    test_set = data.iloc[:foldLen]      # get first fold (test set)
    dataWithoutTestSet = data.iloc[foldLen:]          # remaining data
    return dataWithoutTestSet, test_set

def readGlass():
  regression = False
  columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Class']
  glass_data = pd.read_csv('Glass Data/glass.data', names=columns) # no missing values
  glass_data = glass_data.drop('Id', axis=1)
  glass_data = glass_data.astype(float)
  weights = []
  biases = []
  #for fold in range(10):
  train, test = kfold(glass_data)
  num_nodes = [10]
  weights, biases = NN(train, 1, num_nodes, weights, biases, 'classification')
  numCorrect, total = testNN(test, 1, weights, biases, 'classification')
  print("Accuracy on test set: " + str(numCorrect/total))
  print("Loss: " + str(total-numCorrect))

def readCancer():
  regression = False
  columns = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitosis', 'Class']
  cancer_data = pd.read_csv('Breast Cancer Data/breast-cancer-wisconsin.data', names=columns) # 16 missing values denoted by ?
  cancer_data = cancer_data.replace('?', cancer_data.mode().iloc[0]) # right now replace ? with 5 (middle value of 1-10)
  cancer_data = cancer_data.drop('Sample code number', axis=1)
  cancer_data['Bare Nuclei'] = cancer_data['Bare Nuclei'].astype(int)

  weights = []
  biases = []
  num_nodes = []
  train, test = kfold(cancer_data)
  print("0 Hidden Layers")
  weights, biases = NN(train, 0, num_nodes, weights, biases, 'classification')
  numCorrect, total = testNN(test, 0, weights, biases, 'classification')


  weights = []
  biases = []
  num_nodes = [8]
  train, test = kfold(cancer_data)
  print("1 Hidden Layer")
  weights, biases = NN(train, 1, num_nodes, weights, biases, 'classification')
  numCorrect, total = testNN(test, 1, weights, biases, 'classification')

  weights = []
  biases = []
  num_nodes = [7, 3]
  train, test = kfold(cancer_data)
  print("2 Hidden Layers")
  weights, biases = NN(train, 2, num_nodes, weights, biases, 'classification')
  numCorrect, total = testNN(test, 2, weights, biases, 'classification')

  totalCorrect = 0
  totalOverTen = 0
  weights = []
  biases = []
  print("Ten Fold")
  for fold in range(10):
    train, test = kfold(cancer_data)
    num_nodes = [7, 3]
    weights, biases = NN(train, 2, num_nodes, weights, biases, 'classification')
    numCorrect, total = testNN(test, 2, weights, biases, 'classification')
    totalCorrect += numCorrect
    totalOverTen += total
  print("Average Accuracy on test set: " + str(totalCorrect/totalOverTen))
  print("Average Loss: " + str((totalOverTen-totalCorrect)/10))

def readSoybean():
  regression = False
  columns = ['date','plant-stand','precip','temp','hail','crop-hist','area-damaged','severity','seed-tmt','germination','plant-growth','leaves','leafspots-halo','leafspots-marg','leafspot-size','leaf-shread','leaf-malf','leaf-mild','stem','lodging','stem-cankers','canker-lesion','fruiting-bodies','external decay','mycelium','int-discolor','sclerotia','fruit-pods','fruit spots','seed','mold-growth','seed-discolor','seed-size','shriveling', 'roots', 'Class']
  soybean_data = pd.read_csv('Soybean (small) Data/soybean-small.data', names=columns) # No missing values
  soybean_data = soybean_data.replace('?', soybean_data.mode().iloc[0])
  soybean_data = soybean_data.replace('D1', '1')
  soybean_data = soybean_data.replace('D2', '2')
  soybean_data = soybean_data.replace('D3', '3')
  soybean_data = soybean_data.replace('D4', '4')
  soybean_data = soybean_data.astype(float)

  weights = []
  biases = []
  
  for fold in range(10):
    train, test = kfold(soybean_data)
    num_nodes = [30]
    weights, biases = NN(train, 1, num_nodes, weights, biases, 'classification')
    numCorrect, total = testNN(test, 1, weights, biases, 'classification')
  print("Accuracy on test set: " + str(numCorrect/total))
  print("Loss: " + str(total-numCorrect))

def readAbaloneRegression():

  columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Target']
  abalone_data = pd.read_csv('Abalone (Regression) Data/abalone.data', names=columns)
  abalone_data = abalone_data.replace('M', 0)
  abalone_data = abalone_data.replace('F', 1)
  abalone_data = abalone_data.replace('I', 2)

  weights = []
  biases = []
  for fold in range(10):
    train, test = kfold(abalone_data)
    num_nodes = [5, 2]
    weights, biases = NN(train, 2, num_nodes, weights, biases, 'regression')
    testNN(test, 2, weights, biases, 'regression')


def readComputerHardwareRegression():
  regression = True
  columns = ['Vendor name', 'Model name', 'MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX', 'Target', 'ERP']
  machine_data = pd.read_csv('Computer Hardware (Regression) Data/machine.data', names=columns)
  machine_data = machine_data.drop('Vendor name', axis=1)
  machine_data = machine_data.drop('Model name', axis=1)
  target_column = machine_data.pop("Target")
  machine_data.insert(7, "Target", target_column)

  weights = []
  biases = []
  num_nodes = []
  train, test = kfold(machine_data)
  print("0 Hidden Layers")
  weights, biases = NN(train, 0, num_nodes, weights, biases, 'regression')
  numCorrect, total = testNN(test, 0, weights, biases, 'regression')


  weights = []
  biases = []
  num_nodes = [6]
  train, test = kfold(machine_data)
  print("1 Hidden Layer")
  weights, biases = NN(train, 1, num_nodes, weights, biases, 'regression')
  numCorrect, total = testNN(test, 1, weights, biases, 'regression')

  weights = []
  biases = []
  num_nodes = [5, 2]
  train, test = kfold(machine_data)
  print("2 Hidden Layers")
  weights, biases = NN(train, 2, num_nodes, weights, biases, 'regression')
  numCorrect, total = testNN(test, 2, weights, biases, 'regression')

  totalCorrect = 0
  totalOverTen = 0
  weights = []
  biases = []
  print("Ten Fold")
  for fold in range(10):
    train, test = kfold(machine_data)
    num_nodes = [5, 2]
    weights, biases = NN(train, 2, num_nodes, weights, biases, 'regression')
    numCorrect, total = testNN(test, 2, weights, biases, 'regression')
    totalCorrect += numCorrect
    totalOverTen += total

def readForestFiresRegression():
  regression = True
  columns = ['X', 'Y', 'Month', 'Day', 'FFMC', 'DMC', 'DC', 'ISI', 'Temp', 'RH', 'Wind', 'Rain', 'Target']
  fire_data = pd.read_csv('Forest Fires (Regression) Data/forestfires.csv', names=columns)
  fire_data.drop(index=fire_data.index[0], axis=0, inplace=True) # drop first row 
  fire_data = fire_data.replace(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
  fire_data = fire_data.replace(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'], [1, 2, 3, 4, 5, 6, 7]) # remember that they are cyclical.
  fire_data = fire_data.astype(float)

  weights = [] 
  biases = []
  for fold in range(10):
    train, test = kfold(fire_data)
    num_nodes = [10]
    weights, biases = NN(train, 1, num_nodes, weights, biases, 'regression')
    testNN(test, 1, weights, biases, 'regression')

if __name__ == '__main__':
  readGlass()
  #readSoybean()
  #readAbaloneRegression()
  #readComputerHardwareRegression()
  #readCancer()
  #readForestFiresRegression()