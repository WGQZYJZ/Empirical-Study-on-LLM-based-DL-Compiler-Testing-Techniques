"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn.utils import weight_norm
import torch
input_data = torch.randn(1, 3, 224, 224)
conv1 = torch.nn.Conv2d(3, 16, 3, padding=1)
conv1_with_weight_norm = weight_norm(conv1)
out = conv1_with_weight_norm(input_data)
print(out.shape)