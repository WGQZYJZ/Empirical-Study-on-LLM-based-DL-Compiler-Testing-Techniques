'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([float('-inf'), float('inf'), float('nan')])
output_tensor = torch.Tensor.isneginf(input_tensor)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)
'\nExpected output:\nInput tensor: tensor([-inf,  inf,  nan])\nOutput tensor: tensor([ True, False, False])\n'