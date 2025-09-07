
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2)
        return torch.cat([v] * len([0]))

 # Initializing the model
 m  = Model()
 
 # Input to the model
 x1  = torch.randn(354769187490, 7403238179)
 x2  = torch.randn(x1.size())

 