(batch_size, in_channel, height, width) = (2, 3, 4, 5)
input = torch.randn(batch_size, in_channel, height, width)
output = torch.nn.Softmax2d()(input)