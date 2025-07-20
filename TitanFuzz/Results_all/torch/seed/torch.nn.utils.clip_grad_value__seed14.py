x = torch.randn(3, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
x.grad
x.grad
torch.nn.utils.clip_grad_norm_(x, 0.5)
x.grad
x = torch.randn(3, requires_grad=True)
torch.nn.utils.clip_grad_norm_(x, 0.5)
x.grad