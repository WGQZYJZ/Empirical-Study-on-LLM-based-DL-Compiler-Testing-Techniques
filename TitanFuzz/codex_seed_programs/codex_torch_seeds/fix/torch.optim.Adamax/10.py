'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
X = torch.randn(10, 3)
Y = torch.randn(10, 2)
linear = torch.nn.Linear(3, 2)
adamax = torch.optim.Adamax(linear.parameters(), lr=0.01)
criterion = torch.nn.MSELoss()
for epoch in range(100):
    y_pred = linear(X)
    loss = criterion(y_pred, Y)
    print(epoch, loss.item())