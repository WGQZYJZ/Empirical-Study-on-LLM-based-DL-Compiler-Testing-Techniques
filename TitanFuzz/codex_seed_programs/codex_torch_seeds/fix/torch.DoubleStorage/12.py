'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.DoubleStorage\ntorch.DoubleStorage(*args, **kwargs)\n'
import torch
input_data = [1.0, 2.0, 3.0, 4.0, 5.0]
data_storage = torch.DoubleStorage.from_list(input_data)
print('The type of data_storage: ', type(data_storage))
print('The value of data_storage: ', data_storage)
print('\n')
input_data = [1.0, 2.0, 3.0, 4.0, 5.0]
data_storage = torch.DoubleStorage(input_data)
print('The type of data_storage: ', type(data_storage))
print('The value of data_storage: ', data_storage)