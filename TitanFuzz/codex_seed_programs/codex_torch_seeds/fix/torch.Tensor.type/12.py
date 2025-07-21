'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.randn(20, dtype=torch.float32)
print(input_tensor)
output_tensor = input_tensor.type(torch.int32)
print(output_tensor)