'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
res = torch.broadcast_tensors(a, b)
print('res: ', res)