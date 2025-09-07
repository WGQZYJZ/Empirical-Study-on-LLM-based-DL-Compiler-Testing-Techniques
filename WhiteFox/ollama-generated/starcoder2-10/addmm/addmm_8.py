
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2)
        return v1 + inp

# Initializing the model
m  = Model()

 # Inputs to the model
inp1= torch.randn(64,3).requires_grad_(True), 
 