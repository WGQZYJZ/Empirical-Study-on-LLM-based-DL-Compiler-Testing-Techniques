'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
tensor1 = torch.rand(3, 2)
tensor2 = torch.rand(2, 2)
tensor_row_stack = torch.row_stack((tensor1, tensor2))
print('tensor_row_stack: ', tensor_row_stack)