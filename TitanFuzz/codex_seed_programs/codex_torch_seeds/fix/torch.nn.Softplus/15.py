'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import numpy as np
import torch
np.random.seed(0)
input_data = np.random.randn(5)
input_tensor = torch.tensor(input_data)
softplus = torch.nn.Softplus()
output = softplus(input_tensor)
print(output)