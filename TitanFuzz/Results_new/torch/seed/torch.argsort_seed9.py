input_data = torch.tensor([[1, 3, 5, 7], [2, 4, 6, 8]])
result = torch.argsort(input_data, dim=(- 1), descending=False)