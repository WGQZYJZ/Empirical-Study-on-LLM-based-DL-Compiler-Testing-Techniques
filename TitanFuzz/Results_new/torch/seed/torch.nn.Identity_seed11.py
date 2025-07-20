input_data = torch.randn(3, requires_grad=True)
output = torch.nn.Identity()(input_data)
input_data = torch.randn(1, 2, 3, 4, requires_grad=True)
output = torch.nn.Identity()(input_data)