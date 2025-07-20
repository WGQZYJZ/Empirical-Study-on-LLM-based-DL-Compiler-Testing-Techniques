input_data = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]], dtype=torch.float32)
output = torch.nn.functional.conv1d(input_data, torch.tensor([[[1, 2, 3]]], dtype=torch.float32))