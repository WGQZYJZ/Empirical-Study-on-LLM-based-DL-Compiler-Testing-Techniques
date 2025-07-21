'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvals\ntorch.linalg.eigvals(A, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
eigen_values = torch.linalg.eigvals(input_data)
print(eigen_values)