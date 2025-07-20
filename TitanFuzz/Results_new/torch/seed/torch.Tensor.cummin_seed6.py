_input_tensor = torch.rand(2, 3, 4)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)