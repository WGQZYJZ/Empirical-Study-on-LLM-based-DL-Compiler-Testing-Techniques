'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1.5, 2.7, (- 1.1), (- 0.5)], [0.1, (- 2.3), 4.1, (- 1.0)]])
torch.floor(input_data)