
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_trans = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_trans(x1)
        v2 = F.sigmoid(v1) 
        return v1 * v2


# Initializing the model
m  = Model()

# Inputs to the model