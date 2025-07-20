input_data = torch.randn(2, 3, 3, 3)
norm_layer = torch.nn.InstanceNorm2d(3, affine=True)
output = norm_layer(input_data)