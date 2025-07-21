'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print('input_tensor: \n', input_tensor)
output_tensor = input_tensor.positive()
print('output_tensor: \n', output_tensor)