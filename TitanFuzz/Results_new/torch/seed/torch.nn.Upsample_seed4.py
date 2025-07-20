input = Variable(torch.Tensor(1, 1, 4, 4))
upsample = torch.nn.Upsample(size=None, scale_factor=2, mode='nearest', align_corners=None)
output = upsample(input)