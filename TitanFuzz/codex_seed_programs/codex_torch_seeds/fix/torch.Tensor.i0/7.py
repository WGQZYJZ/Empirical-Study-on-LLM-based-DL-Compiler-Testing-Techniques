'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0\ntorch.Tensor.i0(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
res = torch.Tensor.i0(input_tensor)
print(res)