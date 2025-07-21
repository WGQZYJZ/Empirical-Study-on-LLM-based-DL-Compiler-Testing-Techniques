'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.instance_norm\ntorch.nn.functional.instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(1, 3, 3, 3)
output = nn.functional.instance_norm(input)
print(output)