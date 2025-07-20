input_data = torch.randn(1, 5, 3, 3)
output = torch.nn.Softmax2d()(input_data)