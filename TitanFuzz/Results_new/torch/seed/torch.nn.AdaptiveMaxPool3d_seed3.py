input_data = Variable(torch.randn(1, 3, 5, 5, 5))
pool3d = torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))
output = pool3d(input_data)
input_data = Variable(torch.randn(1, 3, 5, 5, 5))