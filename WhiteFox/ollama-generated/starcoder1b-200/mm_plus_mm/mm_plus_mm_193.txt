
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return torch.addcmul(v1, v1, 1)


# Initializing the model
m = Model()
