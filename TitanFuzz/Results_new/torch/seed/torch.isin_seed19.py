elements = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
test_elements = torch.tensor([0, 2, 4, 6, 8])
result = torch.isin(elements, test_elements)