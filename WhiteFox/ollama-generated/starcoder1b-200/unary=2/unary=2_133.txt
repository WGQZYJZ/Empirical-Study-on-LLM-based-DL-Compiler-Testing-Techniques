
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 3, stride=1, padding=0, output_padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1  * v1  * v1
        v3 = torch.erf(v2) * 0.044715
        v4 = v3  + 1
        v5 = v1  * v4
        v6 = v5  * 0.7978845608028654
        v7 = torch.tanh(v6) + 1
        return v7


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
