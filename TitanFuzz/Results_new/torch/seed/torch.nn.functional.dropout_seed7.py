input_data = torch.randn(10, 1, 1, 3)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True, inplace=False)