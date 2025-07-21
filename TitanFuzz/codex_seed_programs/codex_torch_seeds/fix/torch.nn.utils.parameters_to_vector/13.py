'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
parameters = [torch.randn(3, 4), torch.randn(5, 6), torch.randn(2, 3)]
vector = torch.nn.utils.parameters_to_vector(parameters)
print(vector)
print(vector.shape)