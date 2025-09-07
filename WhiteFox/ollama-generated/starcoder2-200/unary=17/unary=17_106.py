
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convTranspose = torch.nn.ConvTranspose1d(3, 8, kernel_size=4, stride=2)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.convTranspose(x1)
        return self.relu(v1)


# Initializing the model
m = Model2()
 
# Inputs to the model 
x1 = torch.randn(3, 64, 50) # The size of input tensor is (3, 8, 50)
__output__  = m(x1)

