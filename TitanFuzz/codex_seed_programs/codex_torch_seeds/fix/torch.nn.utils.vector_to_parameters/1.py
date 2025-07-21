'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vec, parameters)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
vec = torch.rand(10)
parameters = nn.ParameterList([nn.Parameter(torch.rand(10))])
torch.nn.utils.vector_to_parameters(vec, parameters)
print('parameters:', parameters)