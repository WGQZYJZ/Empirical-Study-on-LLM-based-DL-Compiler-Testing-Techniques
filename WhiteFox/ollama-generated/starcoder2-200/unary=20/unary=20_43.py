
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, kernel_size=10)
 
    def forward(self, x1):
        v1 = convtranspose(x1)
        v2 = torch.sigmoid(v1)

# Initializing the model