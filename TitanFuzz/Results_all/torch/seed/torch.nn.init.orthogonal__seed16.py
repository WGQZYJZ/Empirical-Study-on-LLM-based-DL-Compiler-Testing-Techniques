input_data = Variable(torch.randn(5, 5))
torch.nn.init.orthogonal_(input_data)