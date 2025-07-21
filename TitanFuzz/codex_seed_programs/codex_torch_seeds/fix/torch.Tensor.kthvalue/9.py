'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.kthvalue\ntorch.Tensor.kthvalue(_input_tensor, k, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
output_tensor = torch.Tensor.kthvalue(input_tensor, 1, dim=1, keepdim=False)
print(output_tensor)