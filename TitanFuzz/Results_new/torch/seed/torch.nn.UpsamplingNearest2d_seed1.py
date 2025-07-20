input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
upsampling = torch.nn.UpsamplingNearest2d(scale_factor=2)
output = upsampling(input)