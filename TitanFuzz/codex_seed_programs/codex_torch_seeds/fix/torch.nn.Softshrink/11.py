'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
softshrink = torch.nn.Softshrink(lambd=0.5)
output = softshrink(input_data)
print(output)