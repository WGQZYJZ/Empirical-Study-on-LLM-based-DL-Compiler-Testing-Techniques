'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.split\ntorch.split(tensor, split_size_or_sections, dim=0)\n'
import torch
tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
(t1, t2) = torch.split(tensor, 2, dim=0)
(t3, t4) = torch.split(tensor, 2, dim=1)
print(t1)
print(t2)
print(t3)
print(t4)