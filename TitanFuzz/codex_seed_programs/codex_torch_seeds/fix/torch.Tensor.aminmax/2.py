'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = input_tensor.aminmax()
print(output_tensor)