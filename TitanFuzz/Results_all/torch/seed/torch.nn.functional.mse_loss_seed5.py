input = torch.randn(1, 1, 3, 3)
target = torch.randn(1, 1, 3, 3)
loss = torch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')