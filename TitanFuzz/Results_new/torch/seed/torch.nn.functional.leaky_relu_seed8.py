input_data = torch.randn(2, 2)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)
input_data = torch.randn(2, 2)
torch.nn.functional.elu(input_data, alpha=1.0, inplace=False)