
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2, x3):
        v4 = torch.matmul(x1, x2) # Compute the dot product of a query tensor and a key tensor
        
        v5  = (v4.div_(0.707)).softmax(-1) 
        v6 = torch.nn.functional.dropout(v5, p=0.3)
        v8 = v6.matmul(x3) # Compute the dot product of the dropout output and a value tensor
        
        return v8


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2, 4096) + 573238923
x2  = torch.randn(2, 4096) - 947007029
x3  = torch.randn(2, 1, 4096) * (-0.019375)
__output__  = m(x1, x2, x3)

