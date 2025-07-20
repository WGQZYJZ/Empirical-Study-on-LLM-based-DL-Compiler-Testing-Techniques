input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([[0, 1], [1, 2]], dtype=torch.int64)
output = torch.take(input, index)