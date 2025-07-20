_input_tensor = torch.tensor([[1, 2], [3, 4]])
_output_tensor = torch.Tensor.rot90(_input_tensor, k=1, dims=(0, 1))