'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
tensor_a = torch.randint(0, 2, (3, 3), dtype=torch.bool)
tensor_b = torch.randint(0, 2, (3, 3), dtype=torch.bool)
tensor_c = torch.bitwise_or(tensor_a, tensor_b)
print('tensor_a: ', tensor_a)
print('tensor_b: ', tensor_b)
print('tensor_c: ', tensor_c)