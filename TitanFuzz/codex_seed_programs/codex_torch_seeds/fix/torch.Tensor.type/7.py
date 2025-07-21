'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.type(torch.int32)
print(input_tensor)
print(output_tensor)