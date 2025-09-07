
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        v1 = torch.cat([x1, x2], 0) 
        v2 = v1.view(-1, )
        v3 = torch.tanh(v2).detach() # apply a pointwise unary operation (e.g., ReLU or Tanh)
        return v3


# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(4, )
x2 = torch.randn(5, )

