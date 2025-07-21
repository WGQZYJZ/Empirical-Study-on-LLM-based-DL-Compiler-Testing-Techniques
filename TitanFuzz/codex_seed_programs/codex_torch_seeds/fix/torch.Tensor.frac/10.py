'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
frac_tensor = input_tensor.frac()
print('The input tensor is:', input_tensor)
print('The frac tensor is:', frac_tensor)