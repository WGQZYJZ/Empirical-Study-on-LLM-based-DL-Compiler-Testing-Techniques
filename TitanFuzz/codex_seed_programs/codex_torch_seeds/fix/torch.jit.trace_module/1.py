'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.trace_module\ntorch.jit.trace_module(mod, inputs, optimize=None, check_trace=True, check_inputs=None, check_tolerance=1e-05, strict=True, _force_outplace=False, _module_class=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
input = torch.randn(1, 3, 224, 224, requires_grad=True)
model = torch.jit.trace(nn.Conv2d(3, 64, 3, 1, 1), input)
print(model)