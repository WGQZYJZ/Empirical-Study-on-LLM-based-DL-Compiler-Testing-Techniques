
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(480, 256)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1  *  0.5
        v3  = ((v1 + (v1 ** 3)) * torch.FloatTensor([0.044715]).cuda()) 
        v4  = v3  *  torch.FloatTensor([0.7978845608028654]).cuda()
        v5  = torch.tanh(v4)
        v6  = v5 + 1
        v7  = v2 * v6 
        return v7


# Initializing the model<|end_of_code|>
m = Model().cuda() # Initialize with CUDA support to generate an input tensor on GPU device.

# Inputs to the model<|end_of_code|>
x1  = torch.randn(4, 3, 50, 50).cuda() 

