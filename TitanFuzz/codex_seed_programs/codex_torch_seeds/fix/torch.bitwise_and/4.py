'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
A = torch.tensor([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]], dtype=torch.uint8)
B = torch.tensor([[1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]], dtype=torch.uint8)
C = torch.bitwise_and(A, B)
print(C)
'\nTask 4: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
D = torch.bitwise_or(A, B)
print(D)
'\nTask 5: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
E = torch.bitwise_xor(A, B)
print(E)