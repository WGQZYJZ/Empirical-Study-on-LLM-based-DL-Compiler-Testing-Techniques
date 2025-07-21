'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
print('tensor1 is: ', tensor1)
print('tensor2 is: ', tensor2)
tensor3 = torch.vstack((tensor1, tensor2))
print('tensor3 is: ', tensor3)