'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
import torch.nn as nn
import torch.optim as optim
input_data = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], dtype=torch.float)
output_data = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float)
model = nn.Sequential(nn.Linear(2, 1), nn.Sigmoid())
optimizer = optim.RMSprop(model.parameters(), lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
criterion = nn.BCELoss()
for epoch in range(2000):
    y_pred = model(input_data)
    loss = criterion(y_pred, output_data)