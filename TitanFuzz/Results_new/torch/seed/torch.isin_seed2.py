input_data = [1, 2, 3, 4, 5]
input_data_tensor = torch.tensor(input_data)
test_elements = [1, 2, 3, 4, 5]
test_elements_tensor = torch.tensor(test_elements)
result = torch.isin(input_data_tensor, test_elements_tensor)