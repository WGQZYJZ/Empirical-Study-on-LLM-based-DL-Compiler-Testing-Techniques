data = torch.randn(3, 4)
boundaries = torch.tensor([0.0, 0.5, 1.5])
out = torch.bucketize(data, boundaries)