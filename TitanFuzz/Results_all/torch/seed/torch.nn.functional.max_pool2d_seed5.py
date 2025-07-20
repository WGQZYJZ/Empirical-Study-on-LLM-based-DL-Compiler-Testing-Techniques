input_data = torch.randn(20, 16, 50, 32)
max_pooling_layer = torch.nn.functional.max_pool2d(input_data, kernel_size=2, stride=2, padding=0)