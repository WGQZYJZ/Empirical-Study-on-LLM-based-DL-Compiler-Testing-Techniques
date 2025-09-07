
class Model(torch.nn.Module):
    def __init__(self, dim1):
        super().__init__()
        self.dim1 = dim1
 
    def forward(self, x1, x2):
        result = torch.mm(x1[None], x2)
        return torch.cat([result[:,-1].reshape(-1), result[:,0:self.dim1]])


# Initializing the model
m = Model(64)

# Inputs to the model
inputs  = torch.randn(3, 1, 64, 64)
outputs = m(inputs, inputs).reshape(-1)

