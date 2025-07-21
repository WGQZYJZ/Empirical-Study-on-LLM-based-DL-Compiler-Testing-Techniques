'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vec, parameters)\n'
import torch
vec = torch.randn(10)
parameters = [torch.randn(2, 3), torch.randn(1, 2)]
torch.nn.utils.vector_to_parameters(vec, parameters)
for parameter in parameters:
    print(parameter)