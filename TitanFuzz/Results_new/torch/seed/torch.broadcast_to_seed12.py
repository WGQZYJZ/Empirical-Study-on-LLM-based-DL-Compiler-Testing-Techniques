input = torch.rand(2, 3)
shape = (4, 2, 3)
output = torch.broadcast_to(input, shape)