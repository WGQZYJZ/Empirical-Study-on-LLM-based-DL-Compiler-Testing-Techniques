
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        v2 = torch.cat([v1] * len(input1), dim=1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = [torch.randn(1, 8)] * 3
input2 = [torch.randn(1, 8)] * 3
