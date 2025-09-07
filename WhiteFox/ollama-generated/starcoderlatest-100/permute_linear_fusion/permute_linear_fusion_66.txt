
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor with more than two dimensions (N, H, W, C)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor with less than two dimensions (N*H*W*C,) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 3, 5) # NCHW format
