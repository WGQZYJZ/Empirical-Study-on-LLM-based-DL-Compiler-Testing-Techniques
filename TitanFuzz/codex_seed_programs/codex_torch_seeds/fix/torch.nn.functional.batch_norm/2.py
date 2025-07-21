'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.batch_norm\ntorch.nn.functional.batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 5)
print('Input: ', input)
output = F.batch_norm(input, torch.zeros(3), torch.ones(3), training=True)
print('Output: ', output)