'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
tensor_a = torch.randn(3, 3)
tensor_b = torch.randn(3, 3)
print(torch.row_stack((tensor_a, tensor_b)))