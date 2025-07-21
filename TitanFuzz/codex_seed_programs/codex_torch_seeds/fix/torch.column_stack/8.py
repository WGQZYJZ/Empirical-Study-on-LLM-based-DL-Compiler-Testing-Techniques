'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
tensor_a = torch.rand(3, 4)
tensor_b = torch.rand(3, 4)
tensor_c = torch.rand(3, 4)
tensor_stack = torch.column_stack((tensor_a, tensor_b, tensor_c))
print(tensor_stack)