'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.Tensor(2, 3)
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.float64))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.float32))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.float16))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.int64))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.int32))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.int16))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.int8))
print(input_tensor.new_zeros(input_tensor.size(), dtype=torch.uint8))