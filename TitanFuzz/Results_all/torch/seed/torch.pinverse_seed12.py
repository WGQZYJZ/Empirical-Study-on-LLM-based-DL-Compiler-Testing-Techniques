A = torch.randn(3, 3, requires_grad=True)
pinv_A = torch.pinverse(A)