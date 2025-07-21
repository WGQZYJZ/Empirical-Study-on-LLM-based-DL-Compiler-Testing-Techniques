'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 224, 224)
output = F.adaptive_avg_pool2d(input, (2, 2))
print(output.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 224, 224)