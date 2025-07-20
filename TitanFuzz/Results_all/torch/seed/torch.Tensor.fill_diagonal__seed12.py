_input_tensor = torch.rand(3, 3)
torch.Tensor.fill_diagonal_(_input_tensor, fill_value=1, wrap=False)