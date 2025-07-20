input = torch.randn(2, 2)
output = torch.matrix_exp(input)
expect = torch.tensor([[math.exp(input[0][0]), math.exp(input[0][1])], [math.exp(input[1][0]), math.exp(input[1][1])]])