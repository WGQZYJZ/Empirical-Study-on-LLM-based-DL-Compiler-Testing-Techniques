
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1  = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(4, 8)
y1 = torch.randn(50, 90, 768)
