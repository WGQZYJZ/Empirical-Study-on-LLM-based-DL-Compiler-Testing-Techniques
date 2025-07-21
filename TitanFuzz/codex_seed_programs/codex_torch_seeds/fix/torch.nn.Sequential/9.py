'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
import torch.nn as nn
input_size = 5
output_size = 2
batch_size = 30
hidden_size = 3
input = torch.randn(batch_size, input_size)
print(input)
model = nn.Sequential(nn.Linear(input_size, hidden_size), nn.ReLU(), nn.Linear(hidden_size, output_size), nn.Softmax(dim=1))
print(model)
output = model(input)
print(output)