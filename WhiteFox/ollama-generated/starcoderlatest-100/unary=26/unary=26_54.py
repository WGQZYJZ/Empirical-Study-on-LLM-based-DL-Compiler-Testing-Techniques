
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, kernel_size=(4,4), stride=(4,4), padding=(1,1))
        self.negativelayers = [torch.nn.LeakyReLU(negative_slope)] * 8
 
    def forward(self, x):
        convout = torch.nn.functional.relu(self.conv(x))
        for nl in self.negativelayers:
            convout = nl(convout)
 
        return convout
 
 # Initializing the model
m = Model()

# Inputs to the model
__input_1__  = torch.randn(1, 16, 256, 256)
