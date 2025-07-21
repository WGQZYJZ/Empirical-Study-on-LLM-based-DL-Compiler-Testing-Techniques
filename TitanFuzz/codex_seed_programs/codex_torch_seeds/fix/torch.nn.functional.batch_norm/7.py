'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.batch_norm\ntorch.nn.functional.batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1, eps=1e-05)\n'
import torch
input_data = torch.rand(10, 3, 3, 3)
running_mean = torch.rand(3)
running_var = torch.rand(3)
weight = torch.rand(3)
bias = torch.rand(3)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var, weight, bias, training=True, momentum=0.1, eps=1e-05)
print(output)