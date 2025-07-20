x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
output = distance(x, y)