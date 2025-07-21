'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
input_data = torch.randn(2, 3, 4)
torch.aminmax(input_data, dim=1)
torch.aminmax(input_data, dim=1, keepdim=True)
torch.aminmax(input_data, dim=2)
torch.aminmax(input_data, dim=2, keepdim=True)