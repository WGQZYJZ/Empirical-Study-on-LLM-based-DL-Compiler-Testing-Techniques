_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.cumprod(_input_tensor, dim=1, dtype=torch.float32)