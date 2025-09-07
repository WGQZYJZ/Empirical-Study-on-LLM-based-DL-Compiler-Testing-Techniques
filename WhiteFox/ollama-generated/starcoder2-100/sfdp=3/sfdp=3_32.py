
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query):
        v1  = self.conv(x)
 
        v2  = torch.matmul(v1, v1.transpose(-2, -1))
        v3  = v2.mul(0.5794868851475337)

        v4  = softmax(v3, dim=-1)
        
        v5 = v4 + 1
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(1024)
__output__  = m(x)
 
