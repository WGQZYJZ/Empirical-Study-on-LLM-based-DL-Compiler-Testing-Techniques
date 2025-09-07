
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1)
        v2 = self.conv(x2)
        output = v1 * v2 + (torch.randn_like(v1)) @ (torch.randn_like(v2))  # Note the @ operator in the end of the expression is used to compute the scaled dot product
        return output


# Initializing the model
m = Model()


# Inputs for the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
