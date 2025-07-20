input = torch.tensor([(- 1.0), 0.0, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
boundaries = torch.tensor([1.0, 4.0, 6.0])
output = torch.bucketize(input, boundaries, right=True)
output = torch.bucketize(input, boundaries, right=False)