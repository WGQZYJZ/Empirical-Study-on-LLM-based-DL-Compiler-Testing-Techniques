

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2 
        return v3


# Initializing the model and saving the model to a file.
m = Model()
torch.save(m, 'model_file')


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

