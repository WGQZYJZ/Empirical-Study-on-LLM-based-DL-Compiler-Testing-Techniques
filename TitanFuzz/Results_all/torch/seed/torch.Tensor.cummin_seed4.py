_input_tensor = torch.randint(low=0, high=10, size=(3, 4), dtype=torch.float32)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)