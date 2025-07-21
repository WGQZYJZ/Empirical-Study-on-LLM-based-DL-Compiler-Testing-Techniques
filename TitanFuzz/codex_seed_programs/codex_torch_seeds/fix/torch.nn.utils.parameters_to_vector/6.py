'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
parameters = [torch.randn(1, 2, 3), torch.randn(4, 5, 6)]
parameters_vector = torch.nn.utils.parameters_to_vector(parameters)
print(parameters_vector)