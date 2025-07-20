x = torch.arange(0, 10, dtype=torch.float32)
torch.nn.functional.threshold_(x, threshold=5, value=10)