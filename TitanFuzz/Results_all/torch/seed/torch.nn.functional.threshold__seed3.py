x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.nn.functional.threshold_(x, threshold=3, value=0.5)