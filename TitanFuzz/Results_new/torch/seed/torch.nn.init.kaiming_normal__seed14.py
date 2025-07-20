input_data = torch.randn(1, 3, 224, 224)
tensor = nn.Conv2d(3, 32, 3, padding=1)
torch.nn.init.kaiming_normal_(tensor.weight, a=0, mode='fan_in', nonlinearity='leaky_relu')