_input_tensor = torch.arange(0, 10, dtype=torch.float32)
_output_tensor = torch.Tensor.tile(_input_tensor, dims=(3,))