'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
print(input)
padding = (1, 2)
value = 0
output = torch.nn.ConstantPad1d(padding, value)(input)
print(output)