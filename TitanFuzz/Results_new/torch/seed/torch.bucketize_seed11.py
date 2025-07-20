input = torch.tensor([(- 5), (- 2), 0, 1, 3, 4, 5, 6, 8, 9, 10])
boundaries = torch.tensor([0, 5, 10])
output = torch.bucketize(input, boundaries)