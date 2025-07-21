'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.randn(20, 16, 50, 32, 45)
max_pool_of_tensor = torch.nn.AdaptiveMaxPool3d(output_size=(1, 1, 1))
output = max_pool_of_tensor(input_data)
print(output.shape)
max_pool_of_tensor = torch.nn.AdaptiveMaxPool3d(output_size=(1, 5, 5))
output = max_pool_of_tensor(input_data)
print(output.shape)
max_pool_of_tensor = torch.nn.AdaptiveMaxPool3d(output_size=(5, 1, 1))
output = max_pool_of_tensor(input_data)
print(output.shape)
max_pool_of_tensor = torch.nn.AdaptiveMaxPool3d(output_size=(5, 5, 1))
output = max_pool_of_tensor(input_data)