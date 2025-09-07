
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1000, 2)

    def forward(self, x):
        v = torch.nn.functional.linear(x, self.linear.weight, bias=None) # Linear transformation to the input tensor
        w = v.permute(0, 3, 2, 1)   # Permute the output of the linear transformation
        return w

# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(4, 1000).to_sparse().cuda()
__output__  = m(x)

