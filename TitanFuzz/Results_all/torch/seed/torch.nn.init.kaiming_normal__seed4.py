input_tensor = torch.rand(2, 3, 5, 5)
torch.nn.init.kaiming_normal_(input_tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
input_tensor = torch.rand(2, 3, 5, 5)