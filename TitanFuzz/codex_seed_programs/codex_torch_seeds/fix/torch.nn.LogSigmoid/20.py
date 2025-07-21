'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
input = torch.randn(5)
print(input)
output = torch.nn.LogSigmoid()(input)
print(output)