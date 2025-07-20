batch_size = 128
input_size = 3072
hidden_size = 1024
output_size = 10
x = Variable(torch.randn(batch_size, input_size))
y = Variable(torch.randn(batch_size, output_size), requires_grad=False)
gelu = torch.nn.GELU()
output = gelu(x)