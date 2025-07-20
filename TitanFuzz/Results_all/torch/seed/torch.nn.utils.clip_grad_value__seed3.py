x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 1)
torch.nn.utils.clip_grad_value_(y, 1)