'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
output = torch.Tensor.sub(input_tensor, other)