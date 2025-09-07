
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = x1 * 0.75 + x1 # Multiply the input tensor by a constant (0.75), and then add this result to another tensor 'inp'
        v2 = self.conv1(v1)
        return v2


# Initializing the model