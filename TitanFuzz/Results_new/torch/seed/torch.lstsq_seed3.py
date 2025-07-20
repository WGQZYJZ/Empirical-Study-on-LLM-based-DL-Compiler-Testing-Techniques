input = torch.randn(3, 3, requires_grad=True)
A = torch.randn(3, 3)
torch.lstsq(input, A)