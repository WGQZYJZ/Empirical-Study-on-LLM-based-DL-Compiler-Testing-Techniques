'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], dtype=torch.float32)
output = torch.count_nonzero(input, dim=None)
print('Non-zero count of the input tensor:', output)
output = torch.count_nonzero(input, dim=0)
print('Non-zero count of each column:', output)
output = torch.count_nonzero(input, dim=1)
print('Non-zero count of each row:', output)