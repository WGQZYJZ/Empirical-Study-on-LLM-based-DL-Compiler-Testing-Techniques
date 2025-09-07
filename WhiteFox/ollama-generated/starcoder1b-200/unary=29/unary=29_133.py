
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1, min_value=0, max_value=1):
        return self.conv(x1).clamp_(min_value, max_value)


# Initializing the model
m = Model()


