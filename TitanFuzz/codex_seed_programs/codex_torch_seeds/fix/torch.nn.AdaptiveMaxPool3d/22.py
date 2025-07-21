'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
import torch
input = torch.randn(1, 1, 4, 4, 4)
torch.nn.AdaptiveMaxPool3d(output_size=(2, 2, 2))(input)