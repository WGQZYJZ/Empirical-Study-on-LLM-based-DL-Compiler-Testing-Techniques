
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = v1 * 0.5 + 0.4472136  # Set value of the first element in the input tensor to be equal to 0.44721359

        t2 = torch.cat([t1], dim=0) # Concatenate the result along dimension "0"
        return v, t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
