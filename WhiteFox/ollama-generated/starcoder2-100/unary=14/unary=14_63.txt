
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, kernel_size=(1, 1), stride=1)

    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2 
        return v3


# Initializing the model
m = Model()
__output__  = m(__input__)

