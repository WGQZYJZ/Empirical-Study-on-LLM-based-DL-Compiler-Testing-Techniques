
class Model(torch.nn.Module):
    def __init__(self, shape1, shape2):
        super().__init__()

    def forward(self, x1, x2):
       v = torch.cat([x1, 0.5 * self.weight_const * torch.ones(*shape1), \
            self.bias_const * torch.ones((*shape2))], dim=...)

        v  = v.view((-1,) + shape1)
        v = v * v if self.relu else v
        return v


# Initializing the model
m  = Model((3,5), (7,8)).to(torch.double) # to specify the shapes of input tensors

 # Inputs to the model
    x1= torch.randn(3,4).to(torch.double) 
    x2 = torch.randn(6,7).to(torch.double) 

__output__  = m(x1, x2)

