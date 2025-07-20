input = torch.randn(20, 16, 50, 32, 32)
output = torch.nn.AvgPool3d(kernel_size=(2, 2, 2))(input)
input = torch.randn(20, 16, 50, 32, 32)
output = torch.nn.MaxPool3d(kernel_size=(2, 2, 2))(input)
input = torch.randn(20, 16, 50, 32, 32)
output