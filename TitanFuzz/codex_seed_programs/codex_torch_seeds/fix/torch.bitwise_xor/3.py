'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input1 = torch.randint(0, 2, (3, 3), dtype=torch.long)
input2 = torch.randint(0, 2, (3, 3), dtype=torch.long)
print(input1)
print(input2)
output = torch.bitwise_xor(input1, input2)
print(output)