
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)

        # Uncomment the line to generate the model
        # t1 += other

        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = 5.0 * m.conv._backend_module.weight - 2.7 # The constant 2.7 is just for generating a unique 'other'
