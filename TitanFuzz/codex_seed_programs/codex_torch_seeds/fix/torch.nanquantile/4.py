'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanquantile\ntorch.nanquantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[0.9, 0.9, 0.1], [0.9, 0.1, 0.9], [0.1, 0.9, 0.9]])
output_data = torch.nanquantile(input_data, 0.5, dim=1, keepdim=True)
print(output_data)