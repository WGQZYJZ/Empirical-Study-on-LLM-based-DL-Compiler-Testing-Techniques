'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output = torch.eq(input_data, other_data)
print('output:', output)