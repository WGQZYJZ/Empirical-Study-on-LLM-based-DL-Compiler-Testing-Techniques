input = Variable(torch.randn(1, 10))
output = torch.nn.functional.alpha_dropout(input, p=0.5, training=True)