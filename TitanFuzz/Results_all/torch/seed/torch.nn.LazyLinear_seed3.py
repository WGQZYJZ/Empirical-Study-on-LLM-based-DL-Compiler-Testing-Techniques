input_data = torch.rand(10, 3)
lazy_linear = torch.nn.LazyLinear(3, 2)
output_data = lazy_linear(input_data)