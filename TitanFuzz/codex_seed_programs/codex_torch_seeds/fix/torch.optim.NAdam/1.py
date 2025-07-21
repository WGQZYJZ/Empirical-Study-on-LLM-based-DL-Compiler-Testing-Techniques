'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
import numpy as np
import torch
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
Y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
w = torch.tensor([[0.0]], requires_grad=True)
optimizer = torch.optim.NAdam([w], lr=0.001)
for epoch in range(100):
    y_pred = X.mm(w)
    loss = (y_pred - Y).pow(2).sum()
    print(f'Epoch {(epoch + 1)}/100 | Loss: {loss.item():.4f}')