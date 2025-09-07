
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, x1, -v1 * 0.5 + 0.5) # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        return v2

# Initializing the model
m = Model()

