'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
output = torch.linalg.det(input_data)
print(output)