'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
import torch.nn as nn
import torch.optim as optim
input_data = torch.tensor([[0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 1], [1, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0]], dtype=torch.float)
target_data = torch.tensor([[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1]], dtype=torch.float)
model = nn.Linear(6, 6, bias=False)
optimizer = optim.SparseAdam(model.parameters(), lr=0.01)
for i in range(10000):
    optimizer.zero_grad()
    output = model