x1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
x2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
distance = torch.nn.functional.pairwise_distance(x1, x2)