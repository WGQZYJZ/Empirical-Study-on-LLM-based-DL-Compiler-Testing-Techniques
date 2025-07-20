_input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
_output_tensor = torch.Tensor.unfold(_input_tensor, dimension=0, size=2, step=2)