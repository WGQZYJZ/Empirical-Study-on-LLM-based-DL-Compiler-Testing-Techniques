'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 5)
print(input_tensor)
result = torch.Tensor.argmax(input_tensor, dim=1, keepdim=True)
print(result)