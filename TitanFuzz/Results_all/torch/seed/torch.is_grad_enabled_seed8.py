x = torch.randn(1, requires_grad=True)
with torch.set_grad_enabled(False):
    print(torch.is_grad_enabled())