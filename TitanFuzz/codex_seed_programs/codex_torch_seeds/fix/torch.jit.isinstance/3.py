'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
data = torch.randn(1, 1, 3, 3)
print(data)
print(torch.jit.isinstance(data, torch.Tensor))
print(torch.jit.isinstance(data, torch.FloatTensor))
print(torch.jit.isinstance(data, torch.DoubleTensor))
print(torch.jit.isinstance(data, torch.HalfTensor))
print(torch.jit.isinstance(data, torch.LongTensor))
print(torch.jit.isinstance(data, torch.IntTensor))
print(torch.jit.isinstance(data, torch.ShortTensor))
print(torch.jit.isinstance(data, torch.CharTensor))
print(torch.jit.isinstance(data, torch.ByteTensor))
print(torch.jit.isinstance(data, torch.BoolTensor))