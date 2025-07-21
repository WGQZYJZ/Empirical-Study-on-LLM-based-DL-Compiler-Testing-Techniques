'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.renorm\ntorch.renorm(input, p, dim, maxnorm, *, out=None)\n'
import torch
tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.renorm(tensor_a, p=2, dim=0, maxnorm=1)
tensor_d = torch.renorm(tensor_b, p=2, dim=1, maxnorm=1)
print('tensor_c = ', tensor_c)
print('tensor_d = ', tensor_d)