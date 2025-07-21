'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_data = torch.tensor([[1, 1, 1], [1, 1, 1]])
torch.maximum(input_data, other_data)
torch.max(input_data, other_data)