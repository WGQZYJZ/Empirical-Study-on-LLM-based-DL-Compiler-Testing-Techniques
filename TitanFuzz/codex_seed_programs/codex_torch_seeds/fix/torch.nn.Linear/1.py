'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
y = torch.tensor([[2.0], [3.0]], requires_grad=True)
linear = torch.nn.Linear(2, 1)
print('w: ', linear.weight)
print('b: ', linear.bias)
pred = linear(x)
print('pred: ', pred)
loss = torch.nn.functional.mse_loss(pred, y)
print('loss: ', loss)
loss.backward()
print('dL/dw: ', linear.weight.grad)
print('dL/db: ', linear.bias.grad)
lr = 0.01
linear.weight.data.sub_((lr * linear.weight.grad.data))