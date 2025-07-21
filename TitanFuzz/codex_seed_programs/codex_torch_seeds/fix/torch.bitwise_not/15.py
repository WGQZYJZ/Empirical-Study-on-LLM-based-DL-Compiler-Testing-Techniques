'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_data = torch.randint(0, 2, (2, 3), dtype=torch.uint8)
print(input_data)
output_data = torch.bitwise_not(input_data)
print(output_data)