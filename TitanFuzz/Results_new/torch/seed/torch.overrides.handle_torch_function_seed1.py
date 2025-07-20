x = torch.randn(2, 2)
y = torch.randn(2, 2)
torch.overrides.handle_torch_function(torch.add, (x, y), x, y)