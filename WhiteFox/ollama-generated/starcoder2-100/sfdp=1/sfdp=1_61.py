
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v3 = torch.matmul(x1, x2)  # Compute the dot product of two tensors
        v4 = v3 / math.sqrt(60.)  # Scale by a factor that ensures the sqrt operation is performed over the first dimension
        v5 = v4 + dropout_p 
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
x1, x2  = torch.randn(80, 30), torch.randn(60, 30)
__output__  = m(x1, x2)
 
