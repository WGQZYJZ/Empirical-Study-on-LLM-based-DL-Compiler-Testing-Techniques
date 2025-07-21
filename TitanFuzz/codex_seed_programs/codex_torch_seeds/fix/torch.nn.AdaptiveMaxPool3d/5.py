'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.randn(1, 2, 3, 4, 5)
output = torch.nn.AdaptiveMaxPool3d(output_size=(1, 2, 3))(input_data)
print(output)