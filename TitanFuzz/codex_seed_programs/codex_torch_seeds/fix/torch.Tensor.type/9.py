'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor.type())
print(input_tensor.type(torch.float16))
print(input_tensor.type(torch.float32))
print(input_tensor.type(torch.float64))
print(input_tensor.type(torch.int8))
print(input_tensor.type(torch.int16))
print(input_tensor.type(torch.int32))
print(input_tensor.type(torch.int64))