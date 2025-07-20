input = torch.randn(3, requires_grad=True)
target = torch.randn(3)
loss = torch.nn.functional.smooth_l1_loss(input, target, reduction='mean')