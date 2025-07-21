'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
a = torch.randn(5, requires_grad=True)
b = torch.randn(5, requires_grad=True)
c = torch.randn(5, requires_grad=True)
param_vector = torch.nn.utils.parameters_to_vector([a, b, c])
print(param_vector)