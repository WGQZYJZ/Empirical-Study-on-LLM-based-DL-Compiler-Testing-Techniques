elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output = torch.isin(elements, test_elements)
output = torch.isin(elements, test_elements, invert=True)