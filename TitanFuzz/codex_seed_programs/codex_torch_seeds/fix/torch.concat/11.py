'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
torch.concat((tensor_1, tensor_2), 0)
torch.cat((tensor_1, tensor_2), 0)