'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3)
linear_model = nn.Linear(3, 1)
output = linear_model(input_data)
print(output)
print(linear_model.weight)
print(linear_model.bias)
rand_tensor = torch.randn(1, 3)
rand_tensor_2 = torch.randn(1, 3)
result = (rand_tensor + rand_tensor_2)
print(result)
rand_tensor_3 = torch.randn(3, 3)