_input_tensor = torch.randint(low=0, high=10, size=(3, 4))
_output_tensor = torch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)