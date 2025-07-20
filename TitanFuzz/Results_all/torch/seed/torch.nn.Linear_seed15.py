x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
y = torch.tensor([[2.0], [3.0]], requires_grad=True)
linear = torch.nn.Linear(2, 1)
pred = linear(x)
loss = torch.nn.functional.mse_loss(pred, y)
loss.backward()
lr = 0.01
linear.weight.data.sub_((lr * linear.weight.grad.data))