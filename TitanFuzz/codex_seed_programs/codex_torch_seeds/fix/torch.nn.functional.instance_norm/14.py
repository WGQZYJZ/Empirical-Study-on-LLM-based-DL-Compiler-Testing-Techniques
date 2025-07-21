'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.instance_norm\ntorch.nn.functional.instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input = torch.randn(2, 3, 4, 5)
output = F.instance_norm(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05, elementwise_affine=True)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input = torch.randn(2, 3, 4, 5)