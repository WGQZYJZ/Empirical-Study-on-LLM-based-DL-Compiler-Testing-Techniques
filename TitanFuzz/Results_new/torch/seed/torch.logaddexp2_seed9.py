input = torch.randn(2, 3, dtype=torch.float, requires_grad=True)
other = torch.randn(2, 3, dtype=torch.float, requires_grad=True)
torch.logaddexp2(input, other)