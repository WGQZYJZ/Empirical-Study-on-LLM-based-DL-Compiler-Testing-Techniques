_input_tensor = torch.randint(0, 2, (3, 4, 5), dtype=torch.float)
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)