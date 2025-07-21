'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
input_data = torch.randn(1, 1, 10)
print(input_data)
output = torch.nn.AdaptiveMaxPool1d(3)(input_data)
print(output)
'\nTask 4: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
input_data = torch.randn(1, 1, 10, 10)
print(input_data)
output = torch.nn.AdaptiveMaxPool2d((3, 4))(input_data)
print(output)
'\nTask 5: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
input_data = torch.randn(1, 1, 10, 10, 10)
print(input_data)
output = torch.nn.AdaptiveMaxPool3d((3, 4, 5))(input_data)