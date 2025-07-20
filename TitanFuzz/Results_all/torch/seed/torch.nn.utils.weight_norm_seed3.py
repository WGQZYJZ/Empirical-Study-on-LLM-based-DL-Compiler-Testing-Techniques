input_data = torch.randn(20, 5)
linear = Linear(5, 10)
linear = torch.nn.utils.weight_norm(linear)
output = linear(input_data)