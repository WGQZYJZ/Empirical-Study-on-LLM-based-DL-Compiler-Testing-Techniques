
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        v2 = torch.cat([v1, v1,  ..., v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)
x2 = torch.randn(3, 4, 5)
