
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4) + v1  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m = Model()


