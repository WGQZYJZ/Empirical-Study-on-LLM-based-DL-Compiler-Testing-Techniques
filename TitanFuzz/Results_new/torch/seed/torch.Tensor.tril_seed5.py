_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.tril(_input_tensor, diagonal=0)