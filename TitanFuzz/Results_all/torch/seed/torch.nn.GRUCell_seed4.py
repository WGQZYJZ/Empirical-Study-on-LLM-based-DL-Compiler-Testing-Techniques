x = torch.randn(3, 5)
h = torch.randn(3, 5)
rnn = torch.nn.GRUCell(5, 5)
output = rnn(x, h)