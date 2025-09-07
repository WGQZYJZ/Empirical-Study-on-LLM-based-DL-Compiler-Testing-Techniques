
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v70  = self.conv(x1)
        v69  = v70 * 4 + x1 
        return v70


# Initializing the model
m  = Model()

 # Inputs to the model