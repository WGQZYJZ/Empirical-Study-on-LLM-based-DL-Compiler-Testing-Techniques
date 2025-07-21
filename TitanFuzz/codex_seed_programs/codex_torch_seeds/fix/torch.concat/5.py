'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
import torch
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
tensor_concat_1 = torch.concat((tensor_1, tensor_2), dim=0)
tensor_concat_2 = torch.concat((tensor_1, tensor_2), dim=1)
print('tensor_1:', tensor_1)
print('tensor_2:', tensor_2)
print('tensor_concat_1:', tensor_concat_1)
print('tensor_concat_2:', tensor_concat_2)