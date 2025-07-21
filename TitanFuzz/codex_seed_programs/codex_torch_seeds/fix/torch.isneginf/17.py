'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input_data = torch.tensor([[(- float('inf')), (- float('inf')), (- float('inf'))], [float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan')], [1, 2, 3]])
output_data = torch.isneginf(input_data)
print('input_data:')
print(input_data)
print('output_data:')
print(output_data)