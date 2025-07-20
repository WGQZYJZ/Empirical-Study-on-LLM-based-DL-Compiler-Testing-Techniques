input_data = torch.randn(3, 5, requires_grad=True)
output = torch.pinverse(input_data)
output.backward(torch.ones_like(output))