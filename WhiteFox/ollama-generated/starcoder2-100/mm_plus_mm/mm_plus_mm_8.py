
class Model(torch.nn.Module):
    def __init__(self, c1=None, c2=None, c3=None, c4=None):
        super().__init__()
        self.c1 = torch.nn.Parameter(c1) if isinstance(c1, torch.Tensor) else None
        self.c2 = torch.nn.Parameter(c2) if isinstance(c2, torch.Tensor) else None
        self.c3 = torch.nn.Parameter(c3) if isinstance(c3, torch.Tensor) else None
        self.c4 = torch.nn.Parameter(c4) if isinstance(c4, torch.Tensor) else None
 
    def forward(self, x1):
        v1  = self.conv(x1).relu()
        v2  = torch.mm(v1, v1) + torch.mm(input3, input4)
        return v6


# Initializing the model
m = Model(
    c1=torch.randn(5000), # This tensor is used as a trainable parameter
    c2=torch.randn(5000).requires_grad(),  # This tensor needs to be used in training and should not be optimized for inference
    c3=None, 
    c4=torch.tensor([1., 2., 3., 4., 5.], dtype=torch.float)
)

# Inputs to the model
input3 = torch.randn(6000).requires_grad()
input4 = torch.randn(6000, 6000)

 # Model should be different from the previous one. The parameter `m.c1` should not be the same tensor generated in the previous example but should be a new randomized tensor. The parameter `m.c3` should remain the same as it is given by user. The parameter `m.c4` should also be changed so that the output of the multiplication is different from 5000 values that are all 1.

# Initializing the model (again)
m = Model(
    c2=None, 
    c3=torch.randn(6000), # This tensor is used as a trainable parameter in training and should not be optimized for inference.
    c4=torch.tensor([5., 10., 2., 4.], dtype=torch.float)
)

