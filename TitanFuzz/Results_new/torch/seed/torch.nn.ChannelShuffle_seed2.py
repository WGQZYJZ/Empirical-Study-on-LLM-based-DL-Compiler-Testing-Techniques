input = torch.randn(2, 4, 2, 2)
out = torch.nn.ChannelShuffle(2)(input)