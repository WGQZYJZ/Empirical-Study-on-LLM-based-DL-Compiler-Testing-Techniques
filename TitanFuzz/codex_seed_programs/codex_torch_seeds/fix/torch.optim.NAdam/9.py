'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
data = torch.tensor([[1.0, (- 0.5)], [1.0, 0.5], [1.0, 0.0], [1.0, 1.0]])
target = torch.tensor([[1.0], [0.0], [0.0], [1.0]])
w = torch.tensor([[0.0], [0.0]], requires_grad=True)
b = torch.tensor([[0.0]], requires_grad=True)
optimizer = torch.optim.NAdam([w, b], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
for iter in range(2000):
    y_pred = torch.sigmoid((torch.mm(data, w) + b))