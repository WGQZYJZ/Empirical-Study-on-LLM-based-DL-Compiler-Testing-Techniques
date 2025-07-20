_input_tensor = torch.randint(low=0, high=10, size=(3, 4))
_output_tensor = torch.Tensor.diag(_input_tensor, diagonal=0)