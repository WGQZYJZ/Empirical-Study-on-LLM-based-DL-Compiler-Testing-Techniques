
class Model(torch.nn.Module):
    def __init__(self, n: int = 100):
        super().__init__()
 
    def forward(self, x): 
        v1 = torch.mm(x, x)
        v2 = v1 + 4
        v3 = torch.cat([v1] * n)

        return v3


# Initializing the model
m  = Model() # The number of elements in each batch is 50

# Input to the model
x1 = torch.rand(5, 5)


