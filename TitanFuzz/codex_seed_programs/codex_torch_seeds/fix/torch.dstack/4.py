'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
tensor_1 = torch.randn(2, 3)
tensor_2 = torch.randn(2, 3)
tensor_3 = torch.randn(2, 3)
print('tensor_1: ', tensor_1)
print('tensor_2: ', tensor_2)
print('tensor_3: ', tensor_3)
tensor_stack = torch.dstack((tensor_1, tensor_2, tensor_3))
print('tensor_stack: ', tensor_stack)