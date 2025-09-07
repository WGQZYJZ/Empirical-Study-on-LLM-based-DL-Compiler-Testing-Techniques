
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to an input tensor
        v2  = v1 + 2 
        return v2

# Initializing the model and its parameters
linear_weight = torch.randn(4096, 500).to("cuda")
linear_bias = torch.randn(500)
m = Model()
m.linear = torch.nn.Linear(3 * 32 + 1, 500, bias=False).weight.data  = linear_weight
m.linear = torch.nn.Linear(3 * 32 + 1, 500)

__output__  = m(torch.randn(64 ,3* 32+1))

