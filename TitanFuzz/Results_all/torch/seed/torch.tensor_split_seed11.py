input = torch.randn(20, 16)
(chunk1, chunk2) = torch.tensor_split(input, 2, dim=1)