
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v1 = torch.mm(input1, input2)
        v2 = torch.cat([v1, v1, ..., v1])
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
input1 = torch.randn(3, 8)
input2 = torch.randn(8, 4)
