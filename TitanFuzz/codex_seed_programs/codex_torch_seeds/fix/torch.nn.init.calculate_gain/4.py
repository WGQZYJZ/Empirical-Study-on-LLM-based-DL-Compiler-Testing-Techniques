'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.calculate_gain\ntorch.nn.init.calculate_gain(nonlinearity, param=None)\n'
import torch
nonlinearity = 'relu'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)
print('gain = ', gain)