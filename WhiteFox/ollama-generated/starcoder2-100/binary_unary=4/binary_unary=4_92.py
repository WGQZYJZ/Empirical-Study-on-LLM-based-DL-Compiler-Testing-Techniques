
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3


# Initializing the model
other = torch.randn([]) # Initialize another tensor with a shape of [] to pass it as keyword argument
m = Model(other=other)


# Inputs to the model
x1  = torch.randn(1, 8)
__output__  = m(x1)

