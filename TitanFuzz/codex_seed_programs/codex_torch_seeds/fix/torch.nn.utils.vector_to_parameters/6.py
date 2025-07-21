'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vec, parameters)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 1, 2, 2)
print(input)
parameters = [torch.ones(2, 2, requires_grad=True), torch.ones(1, 1, requires_grad=True)]
vec = torch.cat([p.data.view((- 1)) for p in parameters])
print(vec)
torch.nn.utils.vector_to_parameters(vec, parameters)
print(parameters)