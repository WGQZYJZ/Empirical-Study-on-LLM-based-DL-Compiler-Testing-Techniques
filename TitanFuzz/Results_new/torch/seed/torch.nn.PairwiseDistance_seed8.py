x1 = torch.randn(3, 4)
x2 = torch.randn(3, 4)
torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(x1, x2)