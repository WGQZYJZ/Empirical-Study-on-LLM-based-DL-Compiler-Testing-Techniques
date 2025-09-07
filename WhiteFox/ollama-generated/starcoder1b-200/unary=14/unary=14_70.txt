
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = sigmoid(v1)
        v3 = x1 * v2
        return v3


# Initializing the model
m = Model()


