
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
input_size = (8,3,79,50)
 
x1 = torch.randn(*input_size)
__output__= m(x1).sum()


