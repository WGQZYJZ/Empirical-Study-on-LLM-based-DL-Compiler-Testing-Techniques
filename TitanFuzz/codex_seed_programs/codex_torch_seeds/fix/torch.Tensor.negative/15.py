'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 5)
print('Input Tensor: \n', input_tensor)
output_tensor = input_tensor.negative()
print('Output Tensor: \n', output_tensor)