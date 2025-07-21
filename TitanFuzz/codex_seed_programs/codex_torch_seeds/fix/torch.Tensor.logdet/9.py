'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, 10)
logdet_tensor = input_tensor.logdet()
print('The logdet of input tensor is: \n', logdet_tensor)