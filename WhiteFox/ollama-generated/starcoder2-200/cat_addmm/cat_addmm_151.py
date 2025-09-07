
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t = torch.ones((32, 8)) 
        t = t + self.conv(x)
        return t

# Initializing the model
m = Model()

