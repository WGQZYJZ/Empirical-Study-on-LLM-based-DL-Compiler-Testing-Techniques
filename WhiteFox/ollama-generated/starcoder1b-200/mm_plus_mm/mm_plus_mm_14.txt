
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication between input1 and input2
        v2 = v1 + v2  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()


