input = torch.randn(10)
boundaries = torch.tensor([0.0, 0.5, 1.0])
output = torch.bucketize(input, boundaries)