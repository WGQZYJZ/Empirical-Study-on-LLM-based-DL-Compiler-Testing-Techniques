'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vec, parameters)\n'
import torch
import torch
vec = torch.randn(10)
parameters = [torch.randn(2, 3, requires_grad=True), torch.randn(4, requires_grad=True)]
torch.nn.utils.vector_to_parameters(vec, parameters)
print(parameters[0])
print(parameters[1])