input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_data = torch.all(input_data, dim=0, keepdim=False)
output_data = torch.all(input_data, dim=0, keepdim=True)
output_data = torch.all(input_data, dim=1, keepdim=False)