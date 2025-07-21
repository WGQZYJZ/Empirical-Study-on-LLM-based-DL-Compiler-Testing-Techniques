'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import numpy as np
data = np.array([[(- 1), 1, (- 0.5), 0.5, 0]])
x = torch.from_numpy(data)
y = torch.nn.Softsign()
print(y(x))