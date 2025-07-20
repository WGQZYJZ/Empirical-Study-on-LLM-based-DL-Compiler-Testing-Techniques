dtype = torch.FloatTensor
(N, C_in, C_out, L_in, L_out) = (1, 1, 1, 4, 8)
x = Variable(torch.randn(N, C_in, L_in).type(dtype), requires_grad=True)
weight = Variable(torch.randn(C_in, C_out, 3).type(dtype), requires_grad=True)
bias = Variable(torch.randn(C_out).type(dtype), requires_grad=True)
y = torch.nn.functional.conv_transpose1d(x, weight, bias, stride=2, padding=1, output_padding=1)