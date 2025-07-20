x = torch.empty(5, 3)
torch.nn.init.kaiming_uniform_(x, a=0, mode='fan_in', nonlinearity='leaky_relu')