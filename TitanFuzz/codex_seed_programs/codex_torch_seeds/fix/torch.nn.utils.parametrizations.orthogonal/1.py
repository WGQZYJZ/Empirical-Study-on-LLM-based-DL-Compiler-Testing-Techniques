"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrizations.orthogonal\ntorch.nn.utils.parametrizations.orthogonal(module, name='weight', orthogonal_map=None, *, use_trivialization=True)\n"
import torch
import torch.nn.utils.parametrizations as pt
module = torch.nn.Linear(3, 4)
pt.orthogonal(module, name='weight', orthogonal_map=None, use_trivialization=True)
print(module.weight)