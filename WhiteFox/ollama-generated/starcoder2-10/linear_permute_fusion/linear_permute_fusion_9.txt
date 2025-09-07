
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight) # Apply linear transformation to the input tensor using another parameter
        v2  = v3.permute(-1, -2, )# Permute the permuted output tensor with more than two dimensions

# Initializing model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2)

 __output__  = m(x1)

