
class Model(torch.nn.Module):
    def __init__(self, input1_, input2_, input3_, input4_):
        super().__init__()
        self.mm1 = torch.mm(input1_, input2_)  # Matrix multiplication between input1 and input2
        self.mm2 = torch.mm(input3_, input4_)  # Matrix multiplication between input3 and input4

    def forward(self, x):
        v1  = self.mm1 + self.mm2 
        return v1


# Initializing the model
mm1_ = torch.randn(3072, 56)
mm2_ = torch.randn(56, 498)
m   = Model(mm1_, mm2_)


# Inputs to the model
x1  = torch.randn(1, 3072)
x2  = torch.randn(3072, 56)
x3  = torch.randn(498, 56)
x4  = torch.randn(1, 56)

