'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.logdet(input_tensor)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', output_tensor)