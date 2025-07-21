'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
print(input_data.diff(dim=(- 1)))