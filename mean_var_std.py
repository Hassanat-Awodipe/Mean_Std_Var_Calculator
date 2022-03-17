import numpy as np

try:
  def calculate(list):

    '''This is a calculator that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function will convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary will follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
} '''
    
    user_list = input('\nEnter your list of 9 numbers then press enter: ')
    
    user_list = user_list.split(',')
    user_list = np.array(user_list).astype(float)
    user_arr = user_list.reshape(3,3)
    calculations = {
      '''mean''':[list(user_arr.mean(axis=0)),list(user_arr.mean(axis=1)), user_arr.mean()],
      '''variance''':[list(user_arr.var(axis=0)), list(user_arr.var(axis=1)), user_arr.var()], 
      '''standard deviation''':[list(user_arr.std(axis=0)), list(user_arr.std(axis=1)), user_arr.std()],
      '''max''': [list(map(int, user_arr.max(axis=0))), list(map(int, user_arr.max(axis=1))), int(user_arr.max())], 
      '''min''': [list(map(int, user_arr.min(axis=0))), list(map(int, user_arr.min(axis=1))), int(user_arr.min())], 
      '''sum''': [list(map(int, user_arr.sum(axis=0))), list(map(int, user_arr.sum(axis=1))), int(user_arr.sum())]
                  }
    print('')
    return calculations

  print(calculate(list))

except ValueError:
  print('\nList must contain nine numbers.')

