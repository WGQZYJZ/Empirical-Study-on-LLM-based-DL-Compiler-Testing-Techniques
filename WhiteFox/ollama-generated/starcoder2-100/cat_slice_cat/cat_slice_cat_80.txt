
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        t0 = x[:, 0:9223372036854775807] # A slice of an input tensor along dimension 1
        t1 = self.conv(x) 
        t2 = torch.cat([t0, t1], dim=1) 
        return x

# Initializing the model
m = Model()

