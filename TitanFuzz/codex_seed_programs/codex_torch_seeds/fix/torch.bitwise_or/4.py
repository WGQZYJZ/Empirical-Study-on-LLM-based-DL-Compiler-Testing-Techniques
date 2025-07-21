'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
import torch
input1 = torch.randint(0, 2, (3, 3), dtype=torch.int8)
input2 = torch.randint(0, 2, (3, 3), dtype=torch.int8)
output = torch.bitwise_or(input1, input2)
print('input1:')
print(input1)
print('input2:')
print(input2)
print('output:')
print(output)