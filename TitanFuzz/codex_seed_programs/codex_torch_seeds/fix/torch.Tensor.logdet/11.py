'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
import numpy as np
m = np.random.randint(1, 10)
n = np.random.randint(1, 10)
input_tensor = torch.randn(m, n)
print(torch.Tensor.logdet(input_tensor))