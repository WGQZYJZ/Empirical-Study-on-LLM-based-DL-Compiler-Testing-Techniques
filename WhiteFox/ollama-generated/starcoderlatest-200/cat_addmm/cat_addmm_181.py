
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, torch.tensor([[0., 1.], [3., 4.]]), torch.tensor([[5.], [-6.]]))
        t1 = torch.cat([v1], dim)
        return t1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 3, 4) # The first tensor is concatenated along dimension 0 while the second tensor is concatenated along dimension 1
x2 = torch.randn(2, 2, 5, 6)
