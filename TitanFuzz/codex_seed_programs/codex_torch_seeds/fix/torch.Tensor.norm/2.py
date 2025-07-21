"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.norm\ntorch.Tensor.norm(_input_tensor, p='fro', dim=None, keepdim=False, dtype=None)\n"
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: ', input_tensor)
print('L2 norm: ', input_tensor.norm(p=2))
print('L1 norm: ', input_tensor.norm(p=1))
print('L-infinity norm: ', input_tensor.norm(p=float('inf')))
print('Frobenius norm: ', input_tensor.norm(p='fro'))
print('L2 norm of each column: ', input_tensor.norm(p=2, dim=0))
print('L2 norm of each row: ', input_tensor.norm(p=2, dim=1))
print('L-infinity norm of each column: ', input_tensor.norm(p=float('inf'), dim=0))
print('L-infinity norm of each row: ', input_tensor.norm(p=float('inf'), dim=1))