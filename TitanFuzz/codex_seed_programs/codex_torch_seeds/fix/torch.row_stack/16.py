'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
tensors = (torch.rand(2, 3), torch.rand(2, 3))
out = torch.row_stack(tensors)
print(out)