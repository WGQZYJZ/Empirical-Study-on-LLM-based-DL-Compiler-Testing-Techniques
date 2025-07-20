x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.softplus(x)
y.backward(torch.tensor([1, 1, 1]))