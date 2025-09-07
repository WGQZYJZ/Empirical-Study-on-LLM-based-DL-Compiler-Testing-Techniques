
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
        self.deconv  = torch.nn.ConvTranspose2d(4,9,1,stride=1,padding=1)
 
    def forward(self, x):
        v0  = torch.nn.functional.pad(x,[3],mode="constant")
        v7  = torch.clamp(v0 + 5, min=0 ,max=8) / 9 * self.conv(torch.clamp(v7/2,min=0))
        return v7

# Initializing the model
m1 = Model()

