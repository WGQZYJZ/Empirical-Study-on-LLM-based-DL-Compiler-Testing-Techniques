input = torch.randn(20, 16, 50, 32, 32)
pool = torch.nn.FractionalMaxPool3d(3, output_size=[13, 11, 9])
output = pool(input)