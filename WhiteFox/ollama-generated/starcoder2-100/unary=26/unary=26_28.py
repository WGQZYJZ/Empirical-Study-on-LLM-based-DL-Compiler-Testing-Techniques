
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 4)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope 
        v4 = torch.where(v2, v1, v3 )

# Initializing the model
m  = Model()

 # Inputs to the model