'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vec, parameters)\n'
import torch
x = torch.randn(1, 2, 3)
y = torch.randn(1, 2, 3)
torch.nn.utils.vector_to_parameters(x, y)
print(x)
print(y)