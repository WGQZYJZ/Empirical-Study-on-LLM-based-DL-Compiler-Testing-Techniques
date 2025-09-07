
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) + inp
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 32) # 64 inputs of size 32 by 32 matrix
x2 = torch.randn(64, 32) # 64 inputs of size 32 by 32 matrix
