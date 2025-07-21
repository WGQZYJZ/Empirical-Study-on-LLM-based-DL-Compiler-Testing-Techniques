'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.mul(tensor_a, tensor_b)
print('tensor_c:', tensor_c)