
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1) 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3,8,64,64)


# Running the model on the input tensor and observing the results<|end_of_result|>
__output__  = m(x1).shape
