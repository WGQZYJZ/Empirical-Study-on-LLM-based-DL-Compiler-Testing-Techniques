data = torch.randn(5, 3, requires_grad=True)
result = torch.nn.PairwiseDistance()(data, data)