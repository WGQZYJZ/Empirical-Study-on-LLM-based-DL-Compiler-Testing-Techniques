'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.type(input_tensor, dtype=torch.float32)
print(output_tensor)