
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = F.relu(v1) # The function for ReLU activation is torch.nn.functional (F)
        return v2

m  = Model()
__output__  = m(x1)
