'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 5)
pooling_layer = torch.nn.LPPool1d(norm_type=2, kernel_size=3)
output_tensor = pooling_layer(input_tensor)
print(output_tensor)