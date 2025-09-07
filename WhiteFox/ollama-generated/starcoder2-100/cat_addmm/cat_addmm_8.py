
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dim = dim
 
    def forward(self, x1):
        v0  = torch.randn([4, 7], device='cuda', requires_grad=False) 
        v1  = torch.randn([4, 256], device='cuda', requires_grad=True) 
        v2  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v3  = v2 * 0.7071067811865476 # Multiply the output of the convolution by a constant value `0.7071067811865476` 
        v4  = torch.addmm(v3, v1, v0) # Matrix multiplication with tensor v0 and concatenation along axis=2
        v5  = torch.cat([v4], self.dim)
        return v5

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(8,3,64,64).cuda()
__output__   = m(x1)

