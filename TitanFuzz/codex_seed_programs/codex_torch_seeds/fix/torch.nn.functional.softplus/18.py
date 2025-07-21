'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 1)
print('input_data:', input_data)
output_data = F.softplus(input_data)
print('output_data:', output_data)