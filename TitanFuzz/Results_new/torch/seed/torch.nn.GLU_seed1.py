input_data = Variable(torch.randn(2, 3, 4))
glu = torch.nn.GLU()
output = glu(input_data)