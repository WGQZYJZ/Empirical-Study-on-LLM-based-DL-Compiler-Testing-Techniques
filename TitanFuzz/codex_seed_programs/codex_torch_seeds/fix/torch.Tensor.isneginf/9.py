'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([float('-inf'), float('inf'), float('nan'), float('inf'), float('-inf')])
torch.Tensor.isneginf(input_tensor)