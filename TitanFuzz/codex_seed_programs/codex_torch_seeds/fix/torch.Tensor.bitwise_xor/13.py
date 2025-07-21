'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
a = torch.randint(0, 2, (5, 5), dtype=torch.int32)
b = torch.randint(0, 2, (5, 5), dtype=torch.int32)
c = a.bitwise_xor(b)
print(a)
print(b)
print(c)