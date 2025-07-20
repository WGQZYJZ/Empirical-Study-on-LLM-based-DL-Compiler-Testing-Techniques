input = torch.rand(1, 1, 4, 4)
output = torch.nn.functional.upsample(input, scale_factor=2, mode='bilinear')