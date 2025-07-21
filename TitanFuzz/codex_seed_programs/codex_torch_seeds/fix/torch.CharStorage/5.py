'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.CharStorage\ntorch.CharStorage(*args, **kwargs)\n'
import torch
list_input = [1, 2, 3, 4, 5, 6]
output = torch.CharStorage(list_input)
print('Output: ', output)