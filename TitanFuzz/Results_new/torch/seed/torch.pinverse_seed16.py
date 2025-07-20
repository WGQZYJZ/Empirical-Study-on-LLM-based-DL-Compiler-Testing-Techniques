input = torch.randn(2, 3, requires_grad=True)
pinv_input = torch.pinverse(input)
pinv_input = torch.pinverse(input, rcond=0.001)