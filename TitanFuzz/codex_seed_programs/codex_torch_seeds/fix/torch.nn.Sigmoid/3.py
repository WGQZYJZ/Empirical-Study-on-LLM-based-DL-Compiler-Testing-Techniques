'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sigmoid\ntorch.nn.Sigmoid()\n'
import torch
input = torch.tensor([1.0])
sigmoid = torch.nn.Sigmoid()
output = sigmoid(input)
print(output)