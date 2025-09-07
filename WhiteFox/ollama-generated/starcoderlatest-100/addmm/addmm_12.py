
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        inp = self._inp(v1) # Pass the output of convolution as keyword argument to '_inp' function
        return v6

    def _inp(self, t1):
        v2 = torch.mm(t1, t1)  # Multiply the input tensor by itself 
        v2 += 0.5
        v3 = torch.mm(v2, inp) + 0.5
        return v3
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
