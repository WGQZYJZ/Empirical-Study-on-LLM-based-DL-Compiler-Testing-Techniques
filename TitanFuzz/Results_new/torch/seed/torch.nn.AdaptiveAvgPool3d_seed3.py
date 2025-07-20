input_data = Variable(torch.randn(1, 3, 5, 5, 5))
output = torch.nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))(input_data)