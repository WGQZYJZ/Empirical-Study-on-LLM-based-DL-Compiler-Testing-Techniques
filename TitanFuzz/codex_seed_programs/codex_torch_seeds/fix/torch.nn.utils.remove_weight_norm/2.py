"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.remove_weight_norm\ntorch.nn.utils.remove_weight_norm(module, name='weight')\n"
import torch
from torch.nn.utils import remove_weight_norm
input_data = torch.randn(1, 1, 3, 3)
conv = torch.nn.Conv2d(1, 1, 3)
conv_with_weight_norm = torch.nn.utils.weight_norm(conv)
conv_with_weight_norm.weight_g.data.fill_(1)
conv_with_weight_norm.weight_v.data.fill_(1)
conv_with_weight_norm.bias.data.fill_(0)
conv_without_weight_norm = remove_weight_norm(conv_with_weight_norm)
print(conv_with_weight_norm(input_data))
print(conv_without_weight_norm(input_data))