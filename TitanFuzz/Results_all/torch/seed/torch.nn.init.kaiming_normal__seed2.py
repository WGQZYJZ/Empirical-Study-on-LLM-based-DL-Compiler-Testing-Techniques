input_data = torch.randn(3, 3)
output_data = torch.nn.init.kaiming_normal_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')