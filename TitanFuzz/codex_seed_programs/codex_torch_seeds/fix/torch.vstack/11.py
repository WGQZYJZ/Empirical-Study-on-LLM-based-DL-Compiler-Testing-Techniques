'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
data = torch.rand(10, 3)
print('data: ', data)
data_new = torch.vstack((data, data))
print('data_new: ', data_new)