input_data = torch.randn(3, 3, requires_grad=True)
output = torch.Tensor.greater_equal(input_data, 0)