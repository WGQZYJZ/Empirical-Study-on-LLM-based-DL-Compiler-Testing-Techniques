

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2)
        v1 = torch.cat([v for _ in range(len(x2))], dim=0) # Concatenate the output tensor along dimension 0
        return v1


# Initializing and running the model
m = Model()
x1 = torch.randn((3, 8))
x2 = torch.randn((4, x1.shape[-1]))
vout = m(x1, x2)

