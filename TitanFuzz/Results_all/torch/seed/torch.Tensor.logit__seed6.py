_input_tensor = torch.randn(2, 3, requires_grad=True)
_logit_output = torch.Tensor.logit_(_input_tensor)