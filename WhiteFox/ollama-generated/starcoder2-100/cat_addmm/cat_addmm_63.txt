
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear= torch.nn.Linear(672000, 54955)
 
    def forward(self, x): 
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 .view(-1, 3*8*8) # Flatten the result of the convolution into a single dimension
        v3  = torch.addmm(v2, torch.randn([672000, 54955]), torch.zeros(54955)) 
        # Perform matrix multiplication on the input tensor and randomly generated tensor with a size matching the input tensor
        return self.linear(torch.cat([v3], dim=1))

# Initializing the model
m = Model()
__output__  = m(__input__)

