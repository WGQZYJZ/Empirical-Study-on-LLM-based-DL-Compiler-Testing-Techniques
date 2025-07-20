dtype = torch.FloatTensor
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = Variable(torch.randn(N, D_in).type(dtype), requires_grad=False)
y = Variable(torch.randn(N, D_out).type(dtype), requires_grad=False)
model = torch.nn.GRUCell(D_in, H)