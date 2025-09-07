
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = F.normalize(x, dim=[-2,-1], p=9) 
        v4  = torch.clamp_max(v1 + 6 / 6., min=-3.) # 3 is added to the output of the normalization operation and then the clamp function is used to clamp the output of the addition operation between -3 and 0
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 56, 7) # The shape for the input tensor is [batch size, number of channels in the input tensors, height of the input tensor, width of the input tensor]
 
__output__  = m(x1)

