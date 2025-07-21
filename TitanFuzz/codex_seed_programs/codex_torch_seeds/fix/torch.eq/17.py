'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
other_data = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
result = torch.eq(input_data, other_data)
print(result)