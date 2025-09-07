
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8,3,1)
    
    def forward(self, x):
        v0 = conv_(x)
        v1 = sigmoid_(v0)

# Initializing the model
m = Model()

 # Inputs to the model
 x = torch.randn(1, 3,64, 64)
 
