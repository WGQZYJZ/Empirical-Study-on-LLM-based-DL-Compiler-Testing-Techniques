(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in))
y = Variable(torch.randn(N, D_out), requires_grad=False)
loss_fn = torch.nn.SoftMarginLoss(size_average=None, reduce=None, reduction='mean')