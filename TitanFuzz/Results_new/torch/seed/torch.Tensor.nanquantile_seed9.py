input_tensor = torch.tensor([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0], [12.0, 13.0, 14.0, 15.0]])
torch.Tensor.nanquantile(input_tensor, 0.5, dim=1, keepdim=True)