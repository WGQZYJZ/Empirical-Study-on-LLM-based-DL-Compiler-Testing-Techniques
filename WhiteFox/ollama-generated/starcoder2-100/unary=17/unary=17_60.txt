
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
        v0  = self.convTrans(x)
        return torch.relu(v0), 


# Initializing the model
m  = Model()

 # Inputs to the model (You can use your own input tensor as the inputs of the model.)
x1 = torch.randn(2, 8, 4, 6)
 
 # Outputs from the model.
y1_expected = m(x1)[0]
 

