
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication between input1 and input2
        v2 = torch.mm(x3, x4)  # Matrix multiplication between input3 and input4
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()


