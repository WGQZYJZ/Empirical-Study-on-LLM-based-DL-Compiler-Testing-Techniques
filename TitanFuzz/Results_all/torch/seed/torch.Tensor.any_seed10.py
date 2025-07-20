_input_tensor = torch.randint(low=1, high=5, size=(3, 2, 4))
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
_output_tensor = torch.Tensor.any(_input_tensor, dim=1, keepdim=False)
_output_tensor = torch.Tensor.any(_input_tensor, dim=1, keepdim=True)