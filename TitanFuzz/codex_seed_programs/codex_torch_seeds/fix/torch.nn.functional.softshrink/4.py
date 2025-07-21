'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
import numpy as np
x = torch.tensor(np.arange((- 5), 5, 0.1), dtype=torch.float32)
y = torch.nn.functional.softshrink(x, lambd=0.5)
print(y)