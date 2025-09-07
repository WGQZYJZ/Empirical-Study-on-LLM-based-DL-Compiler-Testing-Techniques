
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.softmax = nn.Softmax(dim=-1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        vk = self.softmax(torch.matmul(v1, x2).mul(1.))
        v2 = torch.nn.functional.dropout(vk, p=0.5)  # Apply dropout to the softmax output
        v3 = x2 * (v2 - 1.)  # Subtract a constant from the output of the dropout to get the residual
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(8, 5, 32, 32)
