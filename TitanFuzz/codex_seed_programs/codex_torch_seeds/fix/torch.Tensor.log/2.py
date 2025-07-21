'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log\ntorch.Tensor.log(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input data: ', input_tensor)
output_tensor = input_tensor.log()
print('Output data: ', output_tensor)