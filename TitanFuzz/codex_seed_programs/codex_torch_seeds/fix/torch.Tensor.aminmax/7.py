'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.aminmax\ntorch.Tensor.aminmax(_input_tensor, *, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
result = input_tensor.aminmax(dim=0)
print('Result: ', result)
result = input_tensor.aminmax(dim=1)
print('Result: ', result)
result = input_tensor.aminmax(dim=1, keepdim=True)
print('Result: ', result)