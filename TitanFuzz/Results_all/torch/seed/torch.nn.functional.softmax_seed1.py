x = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float32)
output = torch.nn.functional.softmax(x, dim=1)