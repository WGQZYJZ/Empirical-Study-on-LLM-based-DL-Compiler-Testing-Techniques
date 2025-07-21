'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_\ntorch.Tensor.less_(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(1, 5)
print(input_tensor)
print(torch.Tensor.less_(input_tensor, 0.5))