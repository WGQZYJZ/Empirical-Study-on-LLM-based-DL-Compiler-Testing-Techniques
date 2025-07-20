_input_tensor = torch.randint(0, 10, (5, 5))
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)