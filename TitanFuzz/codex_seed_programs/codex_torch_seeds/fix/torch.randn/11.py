'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.tensor(1.0)
y = torch.tensor(2.0)
w = torch.tensor(1.0, requires_grad=True)
y_hat = (w * x)
y_hat.backward()
print(w.grad)
x = torch.randn(10, 3)
y = torch.randn(10, 2)
linear = torch.nn.Linear(3, 2)
print('w: ', linear.weight)
print('b: ', linear.bias)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)
pred = linear(x)
loss = criterion(pred, y)
print('loss: ', loss.item())