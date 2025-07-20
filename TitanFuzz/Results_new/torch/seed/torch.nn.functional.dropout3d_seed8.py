input_data = torch.randn(1, 1, 5, 5, 5)
output_data = torch.nn.functional.dropout3d(input=input_data, p=0.5, training=True, inplace=False)