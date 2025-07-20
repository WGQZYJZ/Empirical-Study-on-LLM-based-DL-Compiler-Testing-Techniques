x1 = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4]])
x2 = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4]])
torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)