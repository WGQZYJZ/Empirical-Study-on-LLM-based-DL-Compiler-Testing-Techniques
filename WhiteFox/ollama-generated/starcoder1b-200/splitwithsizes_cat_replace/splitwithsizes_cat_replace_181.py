
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, 4, dim=0)
        print(type(v))
        v_out1 = torch.cat([x1, x1, v[0], v[2]], dim=0)
        return v_out1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
