input_data = torch.randn(2, 3, requires_grad=True)
other_data = torch.randn(3, requires_grad=True)
output = torch.inner(input_data, other_data)