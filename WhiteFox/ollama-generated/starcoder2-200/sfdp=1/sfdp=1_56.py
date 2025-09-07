
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k2, v3):
 
        v1 = torch.matmul(q1, k2.transpose(-2, -1)) 
        v2  = v1 / (0.5) # <||>
        v4 =  v2.softmax(dim=-1) 
        v5=torch.nn.functional.dropout(v4, p=0.7)
        v6 = v5 .matmul(v3 )

        return v6

# Initializing the model
m = Model()

 # Inputs to the model 
x1 = torch.randn(2, 8) 
x2 = torch.randn(4, 3, 8)
x3 = torch.randn(50, 10, 9)
__output__  = m(x1, x2, x3) 
