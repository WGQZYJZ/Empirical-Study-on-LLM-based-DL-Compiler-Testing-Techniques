
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return relu(v1)


# Initializing the model
m = Model()


