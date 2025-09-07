
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 3, 48, 48)
        v2 = (v1  # Cubed
             * 0.044715)  # Multiplied by constant value `0.044715`
         .view(-1, 3, 16, 16)
         .transpose(1, 3)  # Transpose
        v3 = (v2  # Hypotenuse
             * v2)   # Multiplied by a constant value `1.0`
         .view(-1, 3, 8, 8)
        )  # View
        return v3


# Initializing the model
m = Model()


