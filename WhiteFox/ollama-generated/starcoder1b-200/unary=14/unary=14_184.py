
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.sig_m          = torch.nn.Sigmoid()
 
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        return self.sig_m(v1)


# Initializing the model
m  = Model()

