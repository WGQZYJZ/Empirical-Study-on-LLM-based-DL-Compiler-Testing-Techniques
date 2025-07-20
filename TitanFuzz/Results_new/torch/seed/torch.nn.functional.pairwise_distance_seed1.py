x1 = Variable(torch.randn(3, 4))
x2 = Variable(torch.randn(3, 4))
d = torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)