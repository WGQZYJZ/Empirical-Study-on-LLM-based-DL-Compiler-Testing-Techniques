'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
tensor_a = torch.randn(4, 4)
print('tensor_a: ', tensor_a)
tensor_b = torch.fix(tensor_a)
print('tensor_b: ', tensor_b)