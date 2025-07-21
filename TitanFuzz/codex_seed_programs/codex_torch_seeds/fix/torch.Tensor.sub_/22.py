'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.arange(1, 6)
torch.Tensor.sub_(input_tensor, other=torch.ones(5))
print(input_tensor)