'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
_input_tensor = torch.randint(1, 10, (3, 3))
print('Input tensor: ')
print(_input_tensor)
print('Output tensor: ')
print(_input_tensor.values())