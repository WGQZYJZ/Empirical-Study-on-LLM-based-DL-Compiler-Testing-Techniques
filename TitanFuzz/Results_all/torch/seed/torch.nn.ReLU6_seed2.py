input_data = torch.randn(1, 1, 3, 3)
output_data = torch.nn.ReLU6(inplace=False)(input_data)