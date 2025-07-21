input = torch.tensor([[0, 1, 1, 2], [1, 2, 0, 1]])
weight = torch.tensor([[0.1, 0.2, 0.3], [0.2, 0.2, 0.2], [0.3, 0.2, 0.1]])
output = torch.nn.functional.embedding_bag(input, weight, mode='mean')