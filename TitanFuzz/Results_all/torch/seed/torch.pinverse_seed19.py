input = torch.randn(3, 5, dtype=torch.float, requires_grad=True)
pinv_input = torch.pinverse(input)