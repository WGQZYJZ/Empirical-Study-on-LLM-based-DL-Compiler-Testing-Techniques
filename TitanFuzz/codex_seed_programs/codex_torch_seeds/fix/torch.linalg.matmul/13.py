'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
other_data = torch.randn(3, 4)
print(torch.linalg.matmul(input_data, other_data))