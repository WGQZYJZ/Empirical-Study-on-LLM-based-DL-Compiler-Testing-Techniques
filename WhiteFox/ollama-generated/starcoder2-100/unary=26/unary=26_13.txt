
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4
