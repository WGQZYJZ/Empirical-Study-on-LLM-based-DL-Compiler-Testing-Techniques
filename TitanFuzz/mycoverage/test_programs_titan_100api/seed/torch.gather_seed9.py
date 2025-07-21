input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
output = torch.gather(input, 1, torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.int64))
output = torch.gather(input, 0, torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.int64))