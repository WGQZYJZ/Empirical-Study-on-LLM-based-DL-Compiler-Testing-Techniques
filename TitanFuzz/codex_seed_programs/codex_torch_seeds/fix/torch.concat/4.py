'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
tensor_1 = torch.rand(2, 3)
tensor_2 = torch.rand(2, 3)
tensor_3 = torch.rand(2, 3)
concat_1 = torch.concat((tensor_1, tensor_2, tensor_3), dim=0)
print(concat_1)
print(concat_1.size())
concat_2 = torch.cat((tensor_1, tensor_2, tensor_3), dim=0)
print(concat_2)
print(concat_2.size())
concat_3 = torch.cat((tensor_1, tensor_2, tensor_3), dim=1)
print(concat_3)
print(concat_3.size())