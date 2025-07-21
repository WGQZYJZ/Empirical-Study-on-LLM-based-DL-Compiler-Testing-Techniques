'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
input = torch.randn(5)
print(input)
output = torch.nn.functional.relu(input)
print(output)
'\nTask 4: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
input = torch.randn(5)
print(input)
output = torch.nn.functional.relu_(input)
print(output)
'\nTask 5: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
input = torch.randn(5)
print(input)
output = torch.nn.functional.leaky_relu(input)
print(output)
'\nTask 6: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
input = torch