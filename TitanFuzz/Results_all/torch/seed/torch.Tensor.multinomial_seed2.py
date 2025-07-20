_input_tensor = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.2, 0.3, 0.4, 0.5], [0.3, 0.4, 0.5, 0.6]])
_output_tensor = torch.Tensor.multinomial(_input_tensor, 2, replacement=True)