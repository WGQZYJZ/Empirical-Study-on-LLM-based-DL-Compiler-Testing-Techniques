
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
        v1 = self.convT(x) # applying convtranspose to input tensor
        v2 = torch.sigmoid(v1) # applying sigmoid to the output of convtranspose
        return v2


# Initializing the model