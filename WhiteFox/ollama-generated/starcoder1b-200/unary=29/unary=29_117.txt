
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=2, stride=2)
 
    def forward(self, x1, min_value=-0.5, max_value=0.5):
        v1 = self.conv_transpose(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m = Model()


