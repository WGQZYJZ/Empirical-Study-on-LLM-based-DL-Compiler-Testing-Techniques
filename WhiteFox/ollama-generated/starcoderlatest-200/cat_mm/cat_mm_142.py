
class Model(torch.nn.Module):
    def __init__(self, c_in=3, c_out=8, k_size=1, stride=1, padding=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(c_in, c_out, k_size, stride=stride, padding=padding)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.mm(v1, v1)  # Matrix multiplication of two input tensors
        t2 = torch.cat([t1, t1, 0.5 * (t1 ** 3)])
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
