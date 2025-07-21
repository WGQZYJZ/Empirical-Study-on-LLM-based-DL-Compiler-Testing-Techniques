'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_tensor = torch.rand(5, 3)
print('input_tensor:', input_tensor)
frac_tensor = input_tensor.frac()
print('frac_tensor:', frac_tensor)