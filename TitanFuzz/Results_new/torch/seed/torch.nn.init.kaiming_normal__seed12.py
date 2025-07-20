input_data = torch.randn(1, 3, 3, 3)
torch.nn.init.kaiming_normal_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')