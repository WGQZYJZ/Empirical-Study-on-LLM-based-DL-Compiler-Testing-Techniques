'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 5)
print('Input data: ', input_data)
(q_out, r_out) = torch.geqrf(input_data)
print('Q: ', q_out)
print('R: ', r_out)