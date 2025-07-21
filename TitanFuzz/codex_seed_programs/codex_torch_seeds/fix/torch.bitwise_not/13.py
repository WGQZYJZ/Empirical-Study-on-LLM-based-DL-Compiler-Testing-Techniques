'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_data = torch.randint(0, 2, size=(2, 3), dtype=torch.int8)
print(input_data)
output = torch.bitwise_not(input_data)
print(output)