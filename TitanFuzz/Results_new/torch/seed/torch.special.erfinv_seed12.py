input_data = torch.randn(1, requires_grad=True)
output = torch.special.erfinv(input_data)