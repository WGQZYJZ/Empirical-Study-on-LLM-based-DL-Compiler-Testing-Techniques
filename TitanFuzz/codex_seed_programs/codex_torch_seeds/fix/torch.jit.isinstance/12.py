'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
x = torch.randn(4, 4)
print(torch.jit.isinstance(x, torch.Tensor))
print(torch.jit.isinstance(x, torch.FloatTensor))
print(torch.jit.isinstance(x, torch.DoubleTensor))
print(torch.jit.isinstance(x, torch.HalfTensor))
print(torch.jit.isinstance(x, torch.LongTensor))
print(torch.jit.isinstance(x, torch.IntTensor))
print(torch.jit.isinstance(x, torch.ShortTensor))
print(torch.jit.isinstance(x, torch.CharTensor))
print(torch.jit.isinstance(x, torch.ByteTensor))
print(torch.jit.isinstance(x, torch.BoolTensor))