'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch
input = torch.randn(1, 1, 5, 5)
torch.nn.AdaptiveAvgPool2d(output_size=2)(input)
torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(2, 3))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(3, 2))(input)
torch.nn.AdaptiveAvgPool2d(output_size=(3, 3))(input)