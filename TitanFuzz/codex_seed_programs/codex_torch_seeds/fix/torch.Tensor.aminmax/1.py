'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor.aminmax())
print(input_tensor.aminmax(dim=0))
print(input_tensor.aminmax(dim=0, keepdim=True))