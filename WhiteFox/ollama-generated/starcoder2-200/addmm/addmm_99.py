
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 5)

    def forward(self, inp):
        v1  = torch.mm(inp1, inp2)
        v2  = v1 + inp # 'inp' is the input tensor that is passed as a keyword argument 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
inp1 = torch.randn(50, 34)
inp2 = torch.randn(34, 78)
