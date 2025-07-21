'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
tensor_b = torch.tensor([[2, 2, 2], [2, 2, 2]], dtype=torch.float)
print(tensor_a)
print(tensor_b)
print(torch.floor_divide(tensor_a, tensor_b))