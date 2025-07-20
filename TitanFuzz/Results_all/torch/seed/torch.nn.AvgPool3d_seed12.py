input_data = Variable(torch.randn(1, 1, 5, 5, 5))
avgpool3d = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)
output = avgpool3d(input_data)