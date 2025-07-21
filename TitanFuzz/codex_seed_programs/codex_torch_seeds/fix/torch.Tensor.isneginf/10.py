'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- float('inf')), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan')])
print('Input data:')
print(input_tensor)
is_neginf = torch.Tensor.isneginf(input_tensor)
print('Is negative infinity:')
print(is_neginf)