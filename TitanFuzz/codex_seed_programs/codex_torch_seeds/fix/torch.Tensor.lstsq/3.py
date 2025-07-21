'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lstsq\ntorch.Tensor.lstsq(_input_tensor, A)\n'
import torch
A = torch.randn(3, 2)
b = torch.randn(3)
x = torch.Tensor.lstsq(b, A)
print('x is: ', x)