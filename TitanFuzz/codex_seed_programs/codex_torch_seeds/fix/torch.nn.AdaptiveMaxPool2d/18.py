'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.randn(1, 2, 4, 4)
output = torch.nn.AdaptiveMaxPool2d((2, 2))(input_data)
print(output)