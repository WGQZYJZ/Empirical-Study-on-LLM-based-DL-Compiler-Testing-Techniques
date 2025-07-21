input = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]])
weight = torch.rand(10, 3)
output = torch.nn.functional.embedding(input, weight)