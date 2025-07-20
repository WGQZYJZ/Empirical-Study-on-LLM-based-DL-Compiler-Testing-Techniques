input = Variable(torch.randn(10, 10))
torch.nn.init.xavier_normal_(input)