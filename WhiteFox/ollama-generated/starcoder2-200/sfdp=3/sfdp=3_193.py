
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.matmul(x1, y2.transpose(-2,-1))
        v2  = v1 * scale_factor 
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)  
        v5  = v4 .matmul(x1) 
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 8, 12, 12)
y2 = torch.randn(20, 8, 48)
__output__  = m(x1, y2)

