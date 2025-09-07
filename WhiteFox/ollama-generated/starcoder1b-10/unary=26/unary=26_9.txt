
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1 * 0.5, 0)  # Use the mask to multiply each element in the input tensor by 0.5 when v1 is greater than zero
        v3 = v1 * 0.7071067811865476
        v4 = torch.where(v2 > 0, x1, - v3)  # Use the mask to multiply each element in the input tensor by -v3 when v2 is greater than zero
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
