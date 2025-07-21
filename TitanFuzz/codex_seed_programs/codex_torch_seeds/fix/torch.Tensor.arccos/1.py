'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
output = torch.Tensor.arccos(input_data)
print('Input: \n', input_data)
print('Output: \n', output)