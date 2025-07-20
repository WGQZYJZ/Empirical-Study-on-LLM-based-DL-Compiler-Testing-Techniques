input = Variable(torch.Tensor(1, 1, 3, 3))
input[0, 0, :, :] = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
output = upsample(input)