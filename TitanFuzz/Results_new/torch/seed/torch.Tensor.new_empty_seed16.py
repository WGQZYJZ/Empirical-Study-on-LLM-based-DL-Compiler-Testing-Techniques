_input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float32)
_output_tensor = torch.Tensor.new_empty(_input_tensor, (3, 3))