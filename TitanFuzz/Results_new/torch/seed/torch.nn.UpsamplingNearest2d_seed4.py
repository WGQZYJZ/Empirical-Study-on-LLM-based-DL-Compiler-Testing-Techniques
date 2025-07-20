input = Variable(torch.Tensor(1, 1, 5, 5))
upsample = torch.nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(input)