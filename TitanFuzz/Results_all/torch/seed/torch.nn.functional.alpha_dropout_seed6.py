input = Variable(torch.randn(10, 10))
output = torch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)