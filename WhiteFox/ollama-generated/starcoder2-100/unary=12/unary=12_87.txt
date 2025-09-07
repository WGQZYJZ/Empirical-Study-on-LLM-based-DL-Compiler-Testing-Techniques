
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.sig  = torch.nn.Sigmoid()
 
    def forward(self,x1):
        v1 = self.conv(x1) # Apply convolution to the input tensor 
        v2 = self.sig(v1)# Pass through a sigmoid activation function
        v3 = v1 * v2 # Multiply the output of the convolution by the output of the sigmoid function
        return v3


# Initializing the model and setting it to be an optimizer:
m  = Model()
m.eval()
m_optimizer  = torch.optim.Adam(m.parameters())
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


# A sample input to the model:
x2  = torch.randn(10000, 8000).to("cuda") # a 500MB sample to detect memory leaks

