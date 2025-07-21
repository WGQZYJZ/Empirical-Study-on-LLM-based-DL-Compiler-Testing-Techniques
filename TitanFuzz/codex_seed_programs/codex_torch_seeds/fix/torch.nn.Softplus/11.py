'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import numpy as np
data = np.random.randn(10, 10)
tensor = torch.tensor(data)
softplus = torch.nn.Softplus(beta=1, threshold=20)
output = softplus(tensor)
print(output)