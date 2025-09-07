
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, kx2):
        v1  = torch.matmul(x1, kx2)
        v2  = v1 * scale_factor
        v3  = v2.softmax(-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) 
        v5  = v4.matmul(kx2)
        return v5

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(600, 784)
kx2 = torch.randn(3, 784)
 
