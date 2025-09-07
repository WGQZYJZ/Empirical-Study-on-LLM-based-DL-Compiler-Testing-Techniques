
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.mm = torch.ops.aten.mm.default
        self.cat = torch.cat
        self.concat_dim = 3
 
    def forward(self, x1, x2):
        v1 = self.mm(input1, input2)
        v2 = self.cat([v1] * 49, dim=self.concat_dim)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(305, 7864, dtype=torch.float)
x2 = torch.randn(305, 7864, dtype=torch.float)

__output__  = m(x1, x2)

