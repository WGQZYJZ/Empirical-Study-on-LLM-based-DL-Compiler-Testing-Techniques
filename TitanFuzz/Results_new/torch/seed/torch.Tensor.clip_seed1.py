_input_tensor = torch.arange((- 5), 5, 0.1)
_output_tensor = torch.Tensor.clip(_input_tensor, min=(- 3), max=3)