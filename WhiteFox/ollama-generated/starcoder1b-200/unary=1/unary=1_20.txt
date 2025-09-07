
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = (v1 * v1 * v1).mul_(0.044715)
        v4 = ((v3 + v1).mul_(-0.7978845608028654)).tanh_()
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
