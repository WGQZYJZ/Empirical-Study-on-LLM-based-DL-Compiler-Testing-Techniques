'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
import numpy as np
a = np.array([(- 1), (- 0.5), 0, 0.5, 1])
a = torch.from_numpy(a)
print(a)
print(torch.tan(a))