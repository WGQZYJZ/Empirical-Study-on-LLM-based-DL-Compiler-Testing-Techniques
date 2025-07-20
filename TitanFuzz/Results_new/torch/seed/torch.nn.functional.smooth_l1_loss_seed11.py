input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = torch.nn.functional.smooth_l1_loss(input, target)