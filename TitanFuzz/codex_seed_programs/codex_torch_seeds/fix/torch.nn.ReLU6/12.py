'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])
import torch
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])
y = torch.nn.ReLU6()(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
x = torch.tensor([(- 5.0), (- 3.0), 1.0, 3.0, 5.0])
import torch