x = torch.randn(1, 3, requires_grad=True)
y = torch.randn(1, 3, requires_grad=True)
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance(x, y)
distance.backward()