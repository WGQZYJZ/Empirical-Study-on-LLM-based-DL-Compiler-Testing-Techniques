_input_tensor = torch.rand(2, 3, dtype=torch.float32)
_output_tensor = torch.Tensor.reciprocal(_input_tensor)
_output_tensor = torch.reciprocal(_input_tensor)
_input_tensor.reciprocal_()