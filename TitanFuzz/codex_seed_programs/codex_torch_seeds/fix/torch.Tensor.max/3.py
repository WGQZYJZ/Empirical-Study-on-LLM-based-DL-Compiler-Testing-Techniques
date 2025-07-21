'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = input_tensor.max(dim=0)
output_tensor = input_tensor.max(dim=0, keepdim=True)
output_tensor = input_tensor.max(dim=1)
output_tensor = input_tensor.max(dim=1, keepdim=True)
output_tensor = input_tensor.max(dim=2)
output_tensor = input_tensor.max(dim=2, keepdim=True)