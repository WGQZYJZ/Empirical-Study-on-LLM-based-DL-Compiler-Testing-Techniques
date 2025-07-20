input_data = torch.rand(10, requires_grad=True)
output_data = torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)
input_data = torch.rand(10, requires_grad=True)