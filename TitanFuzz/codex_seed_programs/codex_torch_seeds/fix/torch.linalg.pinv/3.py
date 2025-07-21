'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 5)
print('input_data:', input_data)
pinv_data = torch.linalg.pinv(input_data)
print('pinv_data:', pinv_data)