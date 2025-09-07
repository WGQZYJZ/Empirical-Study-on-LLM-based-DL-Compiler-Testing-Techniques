
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v):
        super().__init__()
        self.w = torch.nn.Parameter(torch.randn(d_k, d_v), requires_grad=True)
 
    def forward(self, x, y):
        # We use 1x1 convolution in our model to extract features from input x and target y
        v = torch.matmul(x, self.w)
 
        return v


# Initializing the model
m = Model(50, 50)


# Inputs to the model
x = torch.randn(2, 1, 64, 64)
y = torch.randn(2, 2, 64, 64)
