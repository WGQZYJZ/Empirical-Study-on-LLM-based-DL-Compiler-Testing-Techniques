'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.QInt8Storage\ntorch.QInt8Storage(*args, **kwargs)\n'
import torch
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
storage = torch.QInt8Storage(data)
print('storage = {}'.format(storage))
print('storage.size() = {}'.format(storage.size()))
print('storage.element_size() = {}'.format(storage.element_size()))
print('storage.data_ptr() = {}'.format(storage.data_ptr()))