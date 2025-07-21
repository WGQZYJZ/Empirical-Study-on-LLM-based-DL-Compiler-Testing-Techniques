'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp2\ntorch.exp2(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
output_data = torch.exp2(input_data)
print(output_data)