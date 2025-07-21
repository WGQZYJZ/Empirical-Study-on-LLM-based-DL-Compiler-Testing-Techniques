'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
data = [1, 2, 3]
print(torch.as_tensor(data))
data = [[1, 2], [3, 4]]
print(torch.as_tensor(data))
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(torch.as_tensor(data))