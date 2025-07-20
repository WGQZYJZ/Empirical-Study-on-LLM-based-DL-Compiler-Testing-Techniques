x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.set_warn_always(True)
torch.set_warn_always(False)