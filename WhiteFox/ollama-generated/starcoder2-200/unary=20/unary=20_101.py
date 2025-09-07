
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = convTranspose(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model