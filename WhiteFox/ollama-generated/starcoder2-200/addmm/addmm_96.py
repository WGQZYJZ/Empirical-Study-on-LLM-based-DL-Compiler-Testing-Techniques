
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2=None):
        if inp2:
            t  = torch.mm(inp1, inp2)
        else:
            t = inp + inp1

        return t

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn([3, 5])
