'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = input_tensor.to(torch.float64)
print(output_tensor)