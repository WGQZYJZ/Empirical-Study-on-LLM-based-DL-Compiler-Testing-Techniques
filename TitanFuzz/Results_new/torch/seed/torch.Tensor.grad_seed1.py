_input_tensor = torch.Tensor([[1, 2], [3, 4]])
_grad_output = torch.Tensor([[1, 1], [1, 1]])
_grad_output_tensor = torch.Tensor.grad(_input_tensor, _grad_output)