
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.5)
        v2  = torch.matmul(v1, v1.transpose(-2, -1))
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(4807936, 512)
 
 __output__  = m(x1)
