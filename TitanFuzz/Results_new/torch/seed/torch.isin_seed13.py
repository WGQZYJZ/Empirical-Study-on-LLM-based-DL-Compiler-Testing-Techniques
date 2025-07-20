input = torch.tensor([[1, 2], [3, 4]])
test_elements = torch.tensor([1, 2, 4])
result = torch.isin(input, test_elements)