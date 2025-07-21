'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randint(low=0, high=10, size=(5, 5))
print('Input data: ', input_data)
output_data = torch.randint(low=0, high=10, size=(5, 5))
print('Output data: ', output_data)