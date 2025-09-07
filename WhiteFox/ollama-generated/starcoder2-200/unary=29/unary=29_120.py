
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 16, kernel_size=5)
 
    def forward(self, x1):
        v1  = self.deconv(x1) 
        return  v1


# Initializing the model
m  = Model()

 # Inputs to the model