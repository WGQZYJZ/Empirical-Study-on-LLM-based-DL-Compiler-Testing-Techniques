'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.instance_norm\ntorch.nn.functional.instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn.functional as F
input = torch.randn(4, 4, 5, 5)
print(input.size())
output = F.instance_norm(input)
print(output.size())