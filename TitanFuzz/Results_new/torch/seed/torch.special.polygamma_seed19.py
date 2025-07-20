input_data = Variable(torch.randn(1, 3))
output = torch.special.polygamma(1, input_data)