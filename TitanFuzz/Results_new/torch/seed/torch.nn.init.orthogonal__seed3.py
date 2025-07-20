input_data = Variable(torch.randn(2, 3))
torch.nn.init.orthogonal_(input_data)
torch.nn.init.orthogonal_(input_data, gain=2)