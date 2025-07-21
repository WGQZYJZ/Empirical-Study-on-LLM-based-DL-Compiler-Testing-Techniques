'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.group_norm\ntorch.nn.functional.group_norm(input, num_groups, weight=None, bias=None, eps=1e-05)\n'
import torch
input = torch.randn(4, 4, 4, 4)
input = input.cuda()
num_groups = 2
output = torch.nn.functional.group_norm(input, num_groups)
print(output)