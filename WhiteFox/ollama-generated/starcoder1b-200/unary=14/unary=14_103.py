
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.glu   = torch.nn.GatedLinearUnit()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        glu_out = self.glu(v1)  # Apply the Gated Linear Unit to the output of the convolution
        v2 = glu_out * 0.5
        v3 = glu_out * 0.7071067811865476
        return v3


# Initializing the model
m = Model()


