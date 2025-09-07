
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3,8,10,stride=10)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 50, 50)
 
 # Running the model and getting output
output_from_model  = m(x1)

