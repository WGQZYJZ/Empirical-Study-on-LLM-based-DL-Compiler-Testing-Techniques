input_data = torch.rand(2, 3, 4, 5)
output_data = torch.empty_strided(size=(2, 3, 4, 5), stride=(4, 5, 1, 1))