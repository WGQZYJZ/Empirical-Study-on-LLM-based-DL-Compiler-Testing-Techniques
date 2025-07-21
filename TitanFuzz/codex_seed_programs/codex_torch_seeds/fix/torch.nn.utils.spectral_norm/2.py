"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)\n"
import torch
from torch.nn.utils import spectral_norm
input_data = torch.randn(1, 3, 224, 224)
conv_layer = spectral_norm(torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False))
print(conv_layer)
output_data = conv_layer(input_data)
print(output_data.shape)
linear_layer = spectral_norm(torch.nn.Linear(10, 10, bias=False))
print(linear_layer)
output_data = linear_layer(torch.randn(10))
print(output_data.shape)