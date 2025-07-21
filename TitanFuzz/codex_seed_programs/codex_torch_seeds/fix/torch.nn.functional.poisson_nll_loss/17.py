"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.poisson_nll_loss\ntorch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import numpy as np
input = torch.tensor([1.0, 2.0, 3.0, 4.0])
target = torch.tensor([1.0, 1.0, 1.0, 1.0])
loss = torch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')
print(loss)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight, bias=None, alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None)\n"
import torch
import numpy as np