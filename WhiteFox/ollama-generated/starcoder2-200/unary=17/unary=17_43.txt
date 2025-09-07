
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.deconv = torch.nn.ConvTranspose2d(
            16, 8, kernel_size=3, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.deconv(x)
        v2 = F.relu(v1)
 
        return v2


# Initializing the model