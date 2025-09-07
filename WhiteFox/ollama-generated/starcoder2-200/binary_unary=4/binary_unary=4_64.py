
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # This is the important keyword argument that will be passed to the model
        v3  = torch.nn.functional.relu(v2) # We apply a ReLU to the model result and return it.
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
other  = torch.randn(1, 8).cuda()


x1  = torch.rand((4096), dtype=torch.float) # We generate a random input tensor that is passed as keyword argument `other` to the model.
x1  = torch.cat([ x1 ] * 32, dim=-1 ).reshape(1, 32).cuda()


__output__  = m(x1) # This should produce an error

