input_data = torch.randn(1, 10)
torch.nn.init.kaiming_normal_(input_data, mode='fan_in', nonlinearity='leaky_relu')