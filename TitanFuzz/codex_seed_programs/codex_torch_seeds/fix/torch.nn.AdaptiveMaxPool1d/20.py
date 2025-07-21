'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, 5)
max_pooling = nn.AdaptiveMaxPool1d(2)
print(max_pooling(input_data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, 5, 5)