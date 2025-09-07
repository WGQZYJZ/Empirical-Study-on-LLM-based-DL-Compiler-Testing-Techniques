
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         y = torch.nn.functional.conv3d(x2)  # X should match the conv_3d.
         y = torch.nn.functional.batchnorm3d(y) 
         return y

# Initializing the model
m  = Model()

 # Inputs to the model (assuming we have 5 examples, each of size 1x4x2x6x8 )
for x in range(0 , 5):
    __output__[x]  = m(torch.randn(1, 3, 4, 8))

