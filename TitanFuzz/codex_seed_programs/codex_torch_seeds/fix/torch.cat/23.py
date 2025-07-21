'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
tensor3 = torch.randn(2, 3)
tensor_cat = torch.cat((tensor1, tensor2, tensor3), dim=0)
print(tensor_cat)
print(tensor_cat.shape)