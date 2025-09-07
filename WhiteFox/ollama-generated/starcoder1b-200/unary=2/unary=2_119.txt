
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=2, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 2 * 0.044715
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4) + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


