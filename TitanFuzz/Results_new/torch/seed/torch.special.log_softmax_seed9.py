x = torch.randn(3, requires_grad=True)
y = torch.special.log_softmax(x, dim=0)