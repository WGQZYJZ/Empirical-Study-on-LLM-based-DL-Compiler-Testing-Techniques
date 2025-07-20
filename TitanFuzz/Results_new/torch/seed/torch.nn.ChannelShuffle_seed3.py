input = torch.randn(3, 4, 2, 2)
shuffle = torch.nn.ChannelShuffle(2)
output = shuffle(input)