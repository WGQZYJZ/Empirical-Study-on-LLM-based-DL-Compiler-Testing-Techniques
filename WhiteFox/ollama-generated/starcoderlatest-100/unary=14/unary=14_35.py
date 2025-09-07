
class GLUE_GLU_Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = GLUE_GLU_Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
