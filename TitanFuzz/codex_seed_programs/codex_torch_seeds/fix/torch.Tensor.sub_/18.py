'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[5, 6], [7, 8]])
torch.Tensor.sub_(input_tensor, other)
print(input_tensor)