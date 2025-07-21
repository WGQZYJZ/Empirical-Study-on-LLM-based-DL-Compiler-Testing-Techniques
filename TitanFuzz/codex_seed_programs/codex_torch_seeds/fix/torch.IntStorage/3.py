'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.IntStorage\ntorch.IntStorage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5]
int_storage = torch.IntStorage(input_data)
print('Input data: {}'.format(input_data))
print('IntStorage: {}'.format(int_storage))