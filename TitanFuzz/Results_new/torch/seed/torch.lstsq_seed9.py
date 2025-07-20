input = torch.randn(10, 20, requires_grad=True)
A = torch.randn(10, 10)
torch.lstsq(input, A)