
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).type_as(v1) # Mask to select values from t1 or negative slope based on the condition of t2 in the previous step
        negative_slope = torch.tensor([0], dtype=torch.float32, requires_grad=True)
        v4 = torch.where(mask, v1, v1 * negative_slope) # Multiplication of t1 by negative slope (v3 is negative slope)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__   = m(x1)

