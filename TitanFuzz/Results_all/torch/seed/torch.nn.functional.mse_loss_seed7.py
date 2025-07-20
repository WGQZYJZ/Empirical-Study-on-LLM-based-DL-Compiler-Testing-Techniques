x = Variable(torch.randn(1, 10), requires_grad=True)
y = Variable(torch.randn(1, 10), requires_grad=True)
loss = torch.nn.functional.mse_loss(x, y)
loss.backward()