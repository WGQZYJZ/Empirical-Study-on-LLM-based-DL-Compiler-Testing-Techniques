
class Model(torch.nn.Module):
    def __init__(self, c_dim=32):
        super().__init__()
        self.c_dim = c_dim
 
    def forward(self, x1):
        t1 = torch.mm(input1, input2)
        t2 = torch.cat([t1, t1, 0], dim=self.c_dim) # Concatenation along the dimension specified by `self.c_dim` 
        return t2


# Initializing the model
m = Model(32)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
