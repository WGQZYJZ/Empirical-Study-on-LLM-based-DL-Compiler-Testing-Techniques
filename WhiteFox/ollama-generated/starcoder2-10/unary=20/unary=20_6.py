
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(8, 3, kernelSize=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,8,64,30).to(torch.device("cuda:0"))


__output__  = m(x1)