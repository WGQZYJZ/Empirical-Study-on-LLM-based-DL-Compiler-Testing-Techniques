'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
import torch.nn as nn
import torch
input_size = 10
batch_size = 10
hidden_size = 10
output_size = 10
input_data = torch.randn(batch_size, input_size)
model = nn.Sequential(nn.Linear(input_size, hidden_size), nn.ReLU(), nn.Linear(hidden_size, output_size))
print(model)
print("model's parameters:")
for param in model.parameters():
    print(param)
print("model's modules:")
for module in model.modules():
    print(module)
print("model's named_modules:")