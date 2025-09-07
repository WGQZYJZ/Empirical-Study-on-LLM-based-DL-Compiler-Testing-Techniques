
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1  *  0.5 
        v3  = (v1  **   3 ) # this will be used as constant in the next pattern 
        v4  = ((v3  +   4.76837159e-2)  /    100.)
        v5  = v1  +  v4 
        v6  = (v5  *  0.79788456 ) # this will be used as constant in the next pattern 
        v7  = torch.tanh(v6)  
        v8  = ((v7  +   1 ))
        v9  = (v2  *  v8 )  
        return v9


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1,3 ,64 ,64)
__output__   = m(x1)
 
