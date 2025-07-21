'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
print(x.diff(dim=0))