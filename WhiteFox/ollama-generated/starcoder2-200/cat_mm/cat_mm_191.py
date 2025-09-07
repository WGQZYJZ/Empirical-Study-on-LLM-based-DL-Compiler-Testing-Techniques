
class Model(torch.nn.Module):
    def __init__(self, n, m):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1 for _ in range(n)], dim=0) 
        return v2


# Initializing the model
m  = Model(5, 3) 

# Inputs to the model
x1  = torch.randn(4, 784).t()   # 4 training samples * 784 feature vectors
x2  = torch.randn(784, 60).t()  # 784 input feature vectors * 3 output feature vectors
