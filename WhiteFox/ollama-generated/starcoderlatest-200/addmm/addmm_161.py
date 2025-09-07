
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2=None):
        if inp2 == None:
            v1 = torch.mm(input1, input2)
            v2 = v1 + inp # The tensor 'inp' will be added to the result of matrix multiplication operation
        else: 
            v1 = torch.mm(inp1, inp2) 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
