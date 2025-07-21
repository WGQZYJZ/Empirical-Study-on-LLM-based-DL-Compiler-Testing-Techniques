"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:')
print(input_tensor)
print('Frobenius norm:')
print(input_tensor.norm(p='fro'))
print('L2 norm:')
print(input_tensor.norm(dim=1))
print('L1 norm:')
print(input_tensor.norm(dim=1, p=1))
print('L-infinity norm:')
print(input_tensor.norm(dim=1, p=float('inf')))