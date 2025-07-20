data = torch.randn(3, 4)
boundaries = torch.tensor([0.5, 1.5])
torch.bucketize(input=data, boundaries=boundaries)