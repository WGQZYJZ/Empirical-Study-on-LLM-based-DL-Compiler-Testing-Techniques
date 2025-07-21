'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_data = torch.zeros(input_data.size())
print('Output data:\n', output_data)