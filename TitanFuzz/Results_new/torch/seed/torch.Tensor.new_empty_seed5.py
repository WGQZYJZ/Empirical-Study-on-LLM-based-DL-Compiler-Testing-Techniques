_input_tensor = torch.rand(2, 3, 4)
_output_tensor = torch.Tensor.new_empty(_input_tensor, (2, 3, 4), dtype=torch.float32, device=None, requires_grad=False)