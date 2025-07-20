elements = torch.randint(0, 10, (3, 3))
test_elements = torch.randint(0, 10, (3, 3))
result = torch.isin(elements, test_elements)