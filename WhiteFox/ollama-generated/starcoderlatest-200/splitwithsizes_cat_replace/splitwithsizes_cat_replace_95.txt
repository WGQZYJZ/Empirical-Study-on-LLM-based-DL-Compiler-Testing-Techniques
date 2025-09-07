
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.cat([x1[i] for i in range(x1.size()[0])], dim=0)
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
