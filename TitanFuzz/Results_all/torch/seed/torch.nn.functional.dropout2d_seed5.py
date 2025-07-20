input_data = torch.randn(1, 3, 4, 4)
output_data = torch.nn.functional.dropout2d(input_data, p=0.5, training=True, inplace=False)