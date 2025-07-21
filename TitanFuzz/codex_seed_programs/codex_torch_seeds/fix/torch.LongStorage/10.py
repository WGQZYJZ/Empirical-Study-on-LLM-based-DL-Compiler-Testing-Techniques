'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.LongStorage\ntorch.LongStorage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_data_storage = torch.LongStorage(input_data)
print('Type of input_data_storage: ', type(input_data_storage))
print('input_data_storage: ', input_data_storage)
print('input_data_storage.size(): ', input_data_storage.size())
print('input_data_storage.data_ptr(): ', input_data_storage.data_ptr())