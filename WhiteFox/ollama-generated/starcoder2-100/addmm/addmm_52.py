
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.randn((1,3))
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2)
        return v1 + self.inp


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn([10,8]) # random matrix of size (10 x 8) with values uniformly distributed between -5 and 5.
x2 = torch.randn(7,3, requires_grad=True)

