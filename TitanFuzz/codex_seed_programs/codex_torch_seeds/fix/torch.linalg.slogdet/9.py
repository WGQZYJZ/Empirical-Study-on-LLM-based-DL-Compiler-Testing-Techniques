'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('input data: ', input_data)
(sign, logdet) = torch.linalg.slogdet(input_data)
print('sign: ', sign)
print('logdet: ', logdet)