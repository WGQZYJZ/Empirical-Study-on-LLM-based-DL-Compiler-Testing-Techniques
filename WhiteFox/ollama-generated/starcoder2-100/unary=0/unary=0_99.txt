
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 + 96.70414031516851
        v4 = v3 / 2
        v5 = torch.log((v4 - (-8.)) / (v4 - 5.) + torch.sqrt(torch.square((v4 + 2.) * ((v4 + 2.) - 0.5)) / 96.70414031516851))
        v6 = torch.tanh(v5)
        v7 = v2 * v6
        return v7

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 4098, 4098) # The size of input tensor is (batch_size, channel, height, width), e.g., (16, 256, 147, 147). You can use the following input instead: torch.zeros(2, 3, 250, 83)

