'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
import numpy as np
inp = torch.tensor([[(- 2), (- 1), 0, 1, 2]], dtype=torch.float32)
out = torch.nn.functional.hardshrink(inp, lambd=0.5)
print('Input is:')
print(inp)
print('Output is:')
print(out)