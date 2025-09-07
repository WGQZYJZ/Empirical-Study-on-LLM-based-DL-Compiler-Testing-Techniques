
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.15324816787733793)
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.convtranspose(x)
        v2 = (v1 > 0).float() 
        v3 = - negative_slope
        v4 = torch.where(v2, v1, v3 * v1)
        return v4


# Initializing the model