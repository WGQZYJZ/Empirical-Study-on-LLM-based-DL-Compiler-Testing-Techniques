
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2.transpose(-2, -1))
        v2  = v1 / math.sqrt(x2.size()[-1])
        v3  = torch.nn.functional.softmax(v2) 
        v4  = torch.nn.functional.dropout(v3, p=0.5)  
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(16, 768).cuda() # A query tensor of size (B, C_q), where B is batch dimension, and C_q is the number of channels of the query tensor
x2  = torch.randn(32, 768).cuda()  # A key/value pair tensor of size (B, C) where B is batch dimension and C is the number of channels of the value tensor
__output__  = m(x1, x2)
