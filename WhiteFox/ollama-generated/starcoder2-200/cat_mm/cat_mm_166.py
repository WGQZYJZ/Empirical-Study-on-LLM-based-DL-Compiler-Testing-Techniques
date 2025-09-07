
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.n = n
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2  = torch.cat([v1 for i in range(0, n)], dim=i) # Concatenation of the result tensor along a certain dimension
        return v2

# Initializing the model
m = Model(3).cuda()
x1 = torch.randn(5, 4).cuda()
x2 = torch.randn(4, 6).cuda()
