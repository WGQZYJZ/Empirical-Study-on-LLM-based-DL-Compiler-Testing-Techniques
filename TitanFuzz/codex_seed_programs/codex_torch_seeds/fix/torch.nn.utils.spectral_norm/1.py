"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.spectral_norm\ntorch.nn.utils.spectral_norm(module, name='weight', n_power_iterations=1, eps=1e-12, dim=None)\n"
import torch
from torch import nn
input_data = torch.randn(1, 3, 224, 224)
module = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
sn_module = nn.utils.spectral_norm(module)
output_data = sn_module(input_data)
print('output_data.shape: ', output_data.shape)
print('output_data: ', output_data)