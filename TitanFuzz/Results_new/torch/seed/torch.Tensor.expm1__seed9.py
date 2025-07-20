_input_tensor = Variable(torch.randn(1, 3))
_out_tensor = torch.Tensor.expm1_(_input_tensor)