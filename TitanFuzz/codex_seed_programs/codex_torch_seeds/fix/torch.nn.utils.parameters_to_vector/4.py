'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
import numpy as np
x = torch.randn(2, 3)
print(x)
y = torch.nn.utils.parameters_to_vector(x)
print(y)