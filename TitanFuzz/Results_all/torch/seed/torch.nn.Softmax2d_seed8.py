input_data = torch.randn(2, 3, 3)
output_data = torch.nn.Softmax2d()(input_data)