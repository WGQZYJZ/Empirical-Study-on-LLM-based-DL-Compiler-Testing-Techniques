'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
p1 = torch.randn(3, 3)
p2 = torch.randn(3, 3)
p3 = torch.randn(3, 3)
parameters = [p1, p2, p3]
vector = torch.nn.utils.parameters_to_vector(parameters)
print(vector.shape)