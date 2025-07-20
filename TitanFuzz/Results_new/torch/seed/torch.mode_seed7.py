input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
mode_value = torch.mode(input_data, dim=0, keepdim=False)
mode_value = torch.mode(input_data, dim=0, keepdim=True)