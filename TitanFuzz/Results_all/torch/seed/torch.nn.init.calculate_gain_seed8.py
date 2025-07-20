input_data = torch.randn(1, 1, 3, 3)
gain = torch.nn.init.calculate_gain('relu')
gain = torch.nn.init.calculate_gain('leaky_relu', 0.2)