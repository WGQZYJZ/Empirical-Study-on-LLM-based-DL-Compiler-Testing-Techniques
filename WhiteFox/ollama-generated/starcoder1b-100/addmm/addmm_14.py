
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=torch.ones((3, 4))):
        t1 = torch.mm(x1, x1)
        return inp + t1


# Initializing the model
m = Model()
inp = torch.randn(3, 4)
