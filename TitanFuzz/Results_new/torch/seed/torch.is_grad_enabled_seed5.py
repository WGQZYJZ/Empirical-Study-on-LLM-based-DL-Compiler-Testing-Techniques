input_data = torch.randn(3, requires_grad=True)
with torch.no_grad():
    print(torch.is_grad_enabled())
torch.set_grad_enabled(False)
torch.set_grad_enabled(True)