x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
loss = torch.nn.functional.mse_loss(x, y)