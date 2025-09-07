
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        t1 = torch.cat([v1] * 3, dim=-1)
        return t1
# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(3, 4)
input2 = torch.randn(5, 4)
