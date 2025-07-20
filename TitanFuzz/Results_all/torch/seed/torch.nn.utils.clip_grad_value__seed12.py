x = Variable(torch.randn(1, 1), requires_grad=True)
y = Variable(torch.randn(1, 1), requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
torch.nn.utils.clip_grad_value_(y, 0.5)