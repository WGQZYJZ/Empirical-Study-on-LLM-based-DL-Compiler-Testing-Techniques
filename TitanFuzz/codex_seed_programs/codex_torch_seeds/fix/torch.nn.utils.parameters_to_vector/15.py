'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
import torch.nn as nn
input_data = [torch.rand(4, 4), torch.rand(4, 4), torch.rand(4, 4), torch.rand(4, 4), torch.rand(4, 4)]
result = nn.utils.parameters_to_vector(input_data)
print(result)