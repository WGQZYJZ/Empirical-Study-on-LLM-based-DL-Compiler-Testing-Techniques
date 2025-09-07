
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.ConvTranspose2d(3,8,kernel=5)

    def forward(self, x1):

        t0  = self.conv1d(x1)
        t0 =  t0 * F.sigmoid(t0 ) 
        return t0


# Initializing the model
m  = Model()

# Inputs to the model