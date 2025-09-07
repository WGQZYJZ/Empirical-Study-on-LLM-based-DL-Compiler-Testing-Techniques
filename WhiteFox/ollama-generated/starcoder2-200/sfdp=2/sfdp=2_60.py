
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        t2  = torch.matmul(q1, k1.transpose(-2, -1)) 
        t3  = t2 / scale_factor
        t4  = t3.softmax(dim=-1)
        t5  = t4.dropout(p=0.8) # Apply dropout with the probability of 0.8 to the softmax output
        t6  = torch.matmul(t5, v1)
        return t6

# Initializing the model
m  = Model()
 
# Inputs to the model
i1  = torch.randn(4, 32768)
i2  = torch.randn(4, 3072, 32768)
i3  = torch.randn(4, 3072, 512)
__output__  = m(i1, i2, i3)

