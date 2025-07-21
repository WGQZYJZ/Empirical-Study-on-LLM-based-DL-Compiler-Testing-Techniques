'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
import torch
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = torch.Tensor(data)
result = torch.block_diag(data, data, data)
print(result)