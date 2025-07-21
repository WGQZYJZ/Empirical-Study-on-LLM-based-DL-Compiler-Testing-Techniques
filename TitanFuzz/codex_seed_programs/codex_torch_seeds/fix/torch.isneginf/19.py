'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- float('inf')), float('inf'), float('nan'), 0.0])
is_neginf = torch.isneginf(input_data)
print('is_neginf: ', is_neginf)