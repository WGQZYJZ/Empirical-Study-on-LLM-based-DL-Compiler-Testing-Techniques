x = torch.zeros(5, 5)
torch.nn.init.kaiming_uniform_(x, a=0, mode='fan_in', nonlinearity='leaky_relu')