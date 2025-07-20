input_data = torch.tensor([[0.9, 0.9, 0.1], [0.9, 0.1, 0.9], [0.1, 0.9, 0.9]])
output_data = torch.nanquantile(input_data, 0.5, dim=1, keepdim=True)