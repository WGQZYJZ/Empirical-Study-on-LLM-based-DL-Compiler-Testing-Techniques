
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).mul(0.7071067811865476).exp()
        v3 = (v1 * 0.7071067811865476).log()
        v4 = torch.exp(v2 + v3)  # Compute the error function
        v5 = v4 * v4
        output = (v5 * x1).sum(dim=1, keepdims=True)
        return output


# Initializing the model
m = Model()

