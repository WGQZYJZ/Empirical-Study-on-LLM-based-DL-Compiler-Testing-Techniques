'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torch
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
power_A = torch.linalg.matrix_power(A, 2)
print(power_A)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.norm\ntorch.linalg.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torch