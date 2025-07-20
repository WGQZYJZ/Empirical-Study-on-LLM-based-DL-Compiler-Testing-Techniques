input_data = torch.rand(2, 3)
norm_input_data = torch.linalg.norm(input_data)
norm_input_data_along_0 = torch.linalg.norm(input_data, dim=0)
norm_input_data_along_1 = torch.linalg.norm(input_data, dim=1)