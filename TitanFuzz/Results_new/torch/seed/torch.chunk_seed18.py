x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
chunks = torch.chunk(x, 3, dim=1)
for chunk in chunks:
    print(chunk)