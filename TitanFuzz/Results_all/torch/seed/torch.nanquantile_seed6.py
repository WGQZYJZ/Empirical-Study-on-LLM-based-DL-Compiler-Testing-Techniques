input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
torch.nanquantile(input_data, 0.5, dim=1, keepdim=False, out=None)