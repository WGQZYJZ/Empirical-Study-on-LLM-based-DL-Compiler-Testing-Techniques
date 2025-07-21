"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
input_data = torch.randn(3, 3)
print('input_data: \n', input_data)
eigen_values = torch.linalg.eigvalsh(input_data)
print('eigen_values: \n', eigen_values)