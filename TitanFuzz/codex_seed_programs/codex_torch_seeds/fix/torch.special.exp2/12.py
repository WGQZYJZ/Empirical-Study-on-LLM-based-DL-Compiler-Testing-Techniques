'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4])
result = torch.special.exp2(input_data)
print(result)