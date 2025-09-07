
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.mm(x1, x2) + inp  # Matrix multiplication of two tensors with a keyword argument
        return v


# Initializing the model
m = Model()


# Inputs to the model
inp = torch.randn(3072).cuda().view(8, -1)
input1 = torch.randn(512, 64).cuda()
input2 = torch.randn(1024, 64).cuda()


# Initializing the input tensor for the model
x1 = torch.randn(32, 8*64)


