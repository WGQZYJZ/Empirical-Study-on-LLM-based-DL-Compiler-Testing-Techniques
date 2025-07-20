input = torch.randn(3, requires_grad=True)
target = torch.randn(3)
loss = torch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)