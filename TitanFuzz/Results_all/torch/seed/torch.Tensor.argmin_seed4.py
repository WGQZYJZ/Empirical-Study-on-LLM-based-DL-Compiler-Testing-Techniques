_input_tensor = torch.randint(low=0, high=9, size=(3, 3))
_output_tensor = torch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)