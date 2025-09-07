
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v0  = self.convtranspose(x1)
        v1  = F.relu(v0) 
        return v1


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
