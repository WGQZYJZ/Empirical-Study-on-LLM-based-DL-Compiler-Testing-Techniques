'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(10, 10)
output_tensor = torch.Tensor.aminmax(input_tensor, dim=0, keepdim=True)
print(output_tensor)