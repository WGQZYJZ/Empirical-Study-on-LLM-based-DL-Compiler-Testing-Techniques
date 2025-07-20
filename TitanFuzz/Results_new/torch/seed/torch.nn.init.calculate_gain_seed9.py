nonlinearity = 'linear'
param = None
gain = torch.nn.init.calculate_gain(nonlinearity, param)