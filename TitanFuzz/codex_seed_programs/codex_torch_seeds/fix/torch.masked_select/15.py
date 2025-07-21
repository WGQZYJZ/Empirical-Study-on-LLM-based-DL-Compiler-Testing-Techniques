'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
output = torch.masked_select(input_data, torch.tensor([[0, 1, 0], [1, 1, 1]], dtype=torch.uint8))
print(output)