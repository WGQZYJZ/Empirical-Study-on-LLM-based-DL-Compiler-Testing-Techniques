
class Model(torch.nn.Module):
    def __init__(self, min_value=0.25, max_value=0.75):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value) * 0.7071067811865476 + 1 # Multiply the output of the convolution by 0.7071067811865476
        v3 = torch.clamp_max(v2, max_value) * 0.5 + min_value   # Multiply the output of the previous operation by 0.5 and add it to a minimum value
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
