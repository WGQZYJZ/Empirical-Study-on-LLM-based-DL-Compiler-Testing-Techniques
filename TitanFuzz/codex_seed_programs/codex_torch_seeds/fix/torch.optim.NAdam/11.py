'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
import torch.optim as optim
import numpy as np
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
output_data = np.array([[0], [1], [1], [0]], dtype=np.float32)
input_data = torch.from_numpy(input_data)
output_data = torch.from_numpy(output_data)
optimizer = optim.NAdam([torch.nn.Parameter(torch.randn(2, 3)), torch.nn.Parameter(torch.randn(3, 1))], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
print(optimizer.state_dict())
print(optimizer.state)