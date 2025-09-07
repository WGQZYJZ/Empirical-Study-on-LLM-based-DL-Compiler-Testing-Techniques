
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.convt(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(1,8,64,64)
 
# __output__ is a list of three tensors in this case, one per output from each module.
# To view all the outputs use the .detach().numpy() method.
__output__  = m(x).detach().numpy()
