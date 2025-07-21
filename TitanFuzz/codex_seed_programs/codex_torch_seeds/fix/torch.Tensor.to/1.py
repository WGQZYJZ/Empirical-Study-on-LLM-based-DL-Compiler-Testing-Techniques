'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 3, 3)
output_tensor = input_tensor.to(dtype=torch.int32)
print(output_tensor)