'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
input_data = torch.tensor([[3.0, 3.3], [4.0, 5.9], [6.0, 7.5], [8.1, 9.2], [10.1, 11.3], [12.9, 13.2]], dtype=torch.float32)
output_data = torch.full(size=[6, 2], fill_value=1.0)
print('input_data:', input_data)
print('output_data:', output_data)