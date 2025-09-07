
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return torch.cat([
            x1 * 0.5,  # Multiply each element of the input tensor by 0.5
            x1 * 0.7071067811865476,  # Multiply each element of the input tensor by 0.7071067811865476
            torch.erf(x1 * 0.5)  # Apply the error function to each element of the input tensor
        ], dim=1),


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
