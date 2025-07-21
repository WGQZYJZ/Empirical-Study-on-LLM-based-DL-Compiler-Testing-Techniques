"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 0.0001
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if ((t % 100) == 99):
        print(t, loss.item())
    model.zero_grad()
    loss.backward()
    with torch.no_grad():
        for param in model.parameters():
            param -= (learning_rate * param.grad)