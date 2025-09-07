
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
         v2 = torch.matmul(q1, k1.transpose(-2, -1)) 
         v3 = v2 * 0.9645
         v4 = v3.softmax(dim=-1)
         v5 = v4  + dropout_p
         v7  = v5 @v1
         return v7

# Initializing the model
m  = Model()

# Inputs to the model
q1  = torch.randn(2, 3, 60, 3)
k1  = torch.randn(2, 8, 3, 4)
v1  = torch.randn(2, 90, 50, 7).to('cuda')
 
__output__  = m(q1, k1, v1)

