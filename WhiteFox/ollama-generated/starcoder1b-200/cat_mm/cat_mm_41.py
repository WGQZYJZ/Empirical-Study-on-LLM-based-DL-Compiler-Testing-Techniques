
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return self.concat(v1)
 
    def concat(self, v1):
        if len(v1.shape) > 2:
            v1 = torch.cat(list(filter(lambda x: len(x.shape) == 2, v1)), dim=0)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 8, 8)
x2 = torch.randn(3, 4, 8, 8)
