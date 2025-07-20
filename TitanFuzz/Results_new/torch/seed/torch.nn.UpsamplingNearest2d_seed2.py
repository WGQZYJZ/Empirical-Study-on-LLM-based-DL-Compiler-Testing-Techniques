input = Variable(torch.Tensor([[[[1, 2], [3, 4]]]]))
upsample = torch.nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(input)