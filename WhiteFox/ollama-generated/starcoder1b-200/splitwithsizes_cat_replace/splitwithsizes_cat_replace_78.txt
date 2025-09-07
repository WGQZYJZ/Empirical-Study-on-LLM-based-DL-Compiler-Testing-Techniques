
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Input to the model should be split in batches along dimension 0.
        return torch.split(x1, [4, 6], dim=0)[0] + \
               torch.split(x1, [2, 5], dim=0)[1]


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(3, 4, 64, 64)
__output__     = m(input_tensor)


