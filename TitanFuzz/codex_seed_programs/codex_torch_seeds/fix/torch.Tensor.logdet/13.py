'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(input_tensor)
logdet = input_tensor.logdet()
print('Output tensor:')
print(logdet)