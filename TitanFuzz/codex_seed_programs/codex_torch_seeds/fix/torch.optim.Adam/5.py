'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adam\ntorch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1.0]], dtype=torch.float)
target = torch.tensor([[0], [0], [0], [1.0]], dtype=torch.float)
model = nn.Linear(2, 1)
optimizer = optim.Adam(model.parameters(), lr=0.01)
for epoch in range(100):
    pred = model(data)
    loss = F.mse_loss(pred, target)
    print('Epoch: ', epoch, 'Loss: ', loss.item())
    optimizer.zero_grad