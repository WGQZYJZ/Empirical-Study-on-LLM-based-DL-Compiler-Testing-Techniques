'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
q = torch.tensor([0.5, 0.9])
quantile_result = input_tensor.quantile(q, dim=1, keepdim=True)
print(quantile_result)