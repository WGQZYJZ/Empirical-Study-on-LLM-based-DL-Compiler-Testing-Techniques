'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.Tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
cholesky = torch.Tensor.cholesky(input_tensor, upper=False)
print(cholesky)
'\nExpected output:\ntensor([[ 2.0000,  0.0000,  0.0000],\n        [ 6.0000,  1.0000,  0.0000],\n        [-8.0000,  5.0000,  3.0000]])\n'