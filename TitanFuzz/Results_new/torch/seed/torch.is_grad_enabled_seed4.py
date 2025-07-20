x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
y = torch.tensor([2.0, 2.0, 2.0, 2.0])
torch.set_grad_enabled(False)
torch.set_grad_enabled(True)
with torch.no_grad():
    print(torch.is_grad_enabled())