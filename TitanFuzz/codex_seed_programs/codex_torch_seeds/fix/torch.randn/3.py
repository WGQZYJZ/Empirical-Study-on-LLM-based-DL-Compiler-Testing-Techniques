'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
features = torch.randn((1, 5))
weights = torch.randn_like(features)
bias = torch.randn((1, 1))
'\nTask 1: Calculate the output of this network using the weights and bias tensors\nTask 2: Calculate the output of this network using matrix multiplication\n'
y = ((weights.view(5, 1) * features) + bias)
y = (torch.sum((weights * features)) + bias)
y = (torch.mm(features, weights.view(5, 1)) + bias)
'\nTask 1: Calculate the output of this network using matrix multiplication\nTask 2: Calculate the output of this network using the weights and bias tensors\n'
features = torch.randn((1, 3))
n_input = features.shape[1]
n_hidden = 2
n_output = 1