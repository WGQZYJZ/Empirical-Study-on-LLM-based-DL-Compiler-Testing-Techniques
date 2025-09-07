
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).type(torch.FloatTensor)
        v3 = v1 * -self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 
# Input 0
m.conv.weight.data[0] = 2 * torch.ones_like(m.conv.weight.data)
 
# Input 1 (a constant tensor which is randomly generated at initialization time)
x2  = torch.rand(3, 4, 5).detach().requires_grad_()
 
 
# Initial state of conv layer weights: 
# tensor([[[[[-0.0879]], [-0.1147]], [[-0.6207], [ 0.7634]]]],
 
#         [[[[-0.5556]], [ 0.3573]], [[ 0.7660], [-0.7948]]]])
 
 
# Initial state of conv layer bias: -1.572331428527832
 
# Initial output before backward propagation to the 1st input tensor:  [torch.Size([1, 64, 80, 80]), torch.Size([1, 64, 80, 80]), torch.Size([1, 64, 32, 32])]
 
# Initial output before backward propagation to the 2nd input tensor:  79.5787
 

# Input 0
m.conv.weight.data[0] = -3 * torch.ones_like(m.conv.weight.data)
 
# Input 1 (a constant tensor which is randomly generated at initialization time)
x2  = torch.rand(3, 4, 5).detach().requires_grad_()
 
 
# Initial state of conv layer weights: 
# tensor([[[[[-0.0879]], [-0.1147]], [[-0.6207], [ 0.7634]]]],
 
#         [[[[-0.5556]], [ 0.3573]], [[ 0.7660], [-0.7948]]]])
 
 
# Initial state of conv layer bias: -1.572331428527832
 
# Initial output before backward propagation to the 1st input tensor:   torch.Size([1, 64, 80, 80]), torch.Size([1, 64, 80, 80]), torch.Size([1, 64, 32, 32])]
 
# Initial output before backward propagation to the 2nd input tensor:  79.5787

