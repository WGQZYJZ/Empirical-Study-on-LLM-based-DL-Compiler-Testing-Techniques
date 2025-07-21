"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
input_data = torch.randn(3, 5, requires_grad=True)
target_data = torch.randn(3, 5)
loss = torch.nn.functional.l1_loss(input_data, target_data)
print(loss)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import numpy as np
import torch
input_data = torch.randn(3, 5, requires_grad=True)
target_data = torch.randn(3, 5)