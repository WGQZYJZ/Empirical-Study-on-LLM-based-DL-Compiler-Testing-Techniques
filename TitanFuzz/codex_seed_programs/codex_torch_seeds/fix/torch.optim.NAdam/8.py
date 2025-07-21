'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
import torch.nn as nn
import torch.optim as optim
input_data = torch.randn(2, 2)
target_data = torch.randn(2, 2)
model = nn.Linear(2, 2)
optimizer = optim.NAdam(model.parameters(), lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
for i in range(100):
    optimizer.zero_grad()
    output = model(input_data)
    loss = nn.MSELoss()(output, target_data)
    loss.backward()
    optimizer.step()
    print(loss.item())