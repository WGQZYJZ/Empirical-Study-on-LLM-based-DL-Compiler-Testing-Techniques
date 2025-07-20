x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]))
loss = torch.nn.functional.smooth_l1_loss(x, y)