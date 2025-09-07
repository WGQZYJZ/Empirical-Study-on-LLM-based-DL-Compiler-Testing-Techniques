
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + self.other


# Initializing the model
m = Model()
m_2 = Model(torch.tensor([[0]]).float()) # Initialize a Tensor object of size (1, 3, 64, 64) with value 0
