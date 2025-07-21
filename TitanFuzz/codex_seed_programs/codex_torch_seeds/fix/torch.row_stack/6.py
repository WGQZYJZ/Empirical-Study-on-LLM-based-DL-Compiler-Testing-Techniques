'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
tensor_1 = torch.randn(3, 2)
tensor_2 = torch.randn(3, 2)
print(tensor_1)
print(tensor_2)
tensor_3 = torch.row_stack((tensor_1, tensor_2))
print(tensor_3)