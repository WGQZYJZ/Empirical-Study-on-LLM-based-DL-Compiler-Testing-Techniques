'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.calculate_gain\ntorch.nn.init.calculate_gain(nonlinearity, param=None)\n'
import torch
x = torch.randn(2, 3)
print(torch.nn.init.calculate_gain('leaky_relu'))
print(torch.nn.init.calculate_gain('relu'))
print(torch.nn.init.calculate_gain('sigmoid'))
print(torch.nn.init.calculate_gain('tanh'))
print(torch.nn.init.calculate_gain('linear'))