input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = torch.nn.functional.soft_margin_loss(input, target)