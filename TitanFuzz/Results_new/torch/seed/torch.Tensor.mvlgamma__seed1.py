_input_tensor = Variable(torch.randn(4, 4))
p = 3
torch.Tensor.mvlgamma_(_input_tensor, p)