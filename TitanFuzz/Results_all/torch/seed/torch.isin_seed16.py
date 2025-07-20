elements = torch.tensor([1, 2, 3, 4, 5, 6])
test_elements = torch.tensor([1, 2, 4, 8])
result = torch.isin(elements, test_elements)