'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
tensor_1 = torch.rand(2, 2)
tensor_2 = torch.rand(2, 2)
tensor_3 = torch.rand(2, 2)
result = torch.dstack((tensor_1, tensor_2, tensor_3))
print(result)