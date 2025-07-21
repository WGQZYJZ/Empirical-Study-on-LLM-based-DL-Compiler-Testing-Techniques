'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_or\ntorch.bitwise_or(input, other, *, out=None)\n'
import torch
data_1 = torch.randint(0, 2, (2, 2))
data_2 = torch.randint(0, 2, (2, 2))
print(data_1)
print(data_2)
print(torch.bitwise_or(data_1, data_2))