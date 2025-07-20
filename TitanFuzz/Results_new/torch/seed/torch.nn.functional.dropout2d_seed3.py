input_data = Variable(torch.randn(1, 1, 3, 3))
output_data = torch.nn.functional.dropout2d(input_data, p=0.5, training=True, inplace=False)