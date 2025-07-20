input = torch.randn(1, 3)
output = torch.special.log_softmax(input, dim=0)
output = nn.LogSoftmax(dim=0)(input)