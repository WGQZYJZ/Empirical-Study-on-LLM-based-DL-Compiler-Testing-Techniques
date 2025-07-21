'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
print(input_tensor)
trunc_tensor = torch.Tensor.trunc(input_tensor)
print(trunc_tensor)
trunc_tensor = torch.trunc(input_tensor)
print(trunc_tensor)