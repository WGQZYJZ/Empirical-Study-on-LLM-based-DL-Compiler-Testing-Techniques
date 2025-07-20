x1 = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], dtype=torch.float32)
x2 = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], dtype=torch.float32)
torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)