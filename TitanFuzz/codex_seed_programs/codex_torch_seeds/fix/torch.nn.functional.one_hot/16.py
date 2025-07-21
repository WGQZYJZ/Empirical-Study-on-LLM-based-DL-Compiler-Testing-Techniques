'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import torch.nn.functional as F
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_data = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
print('Input data: ', input_data)
print('\nTask 3: Call the API torch.nn.functional.one_hot')
output = F.one_hot(input_data, num_classes=6)
print('Output: ', output)
print('\nTask 4: Call the API torch.nn.functional.one_hot with a tensor of type torch.long')
input_data_long = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]], dtype=torch.long)