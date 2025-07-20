x = Variable(torch.Tensor([1]), requires_grad=True)
y = Variable(torch.Tensor([2]), requires_grad=True)
loss = torch.nn.functional.mse_loss(x, y)