
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + kwargs['other']
        return v2

# Initializing the model with a "keyword argument" (the 'other' tensor in this example).
m  = Model(other=torch.randn([4,8]))

# Inputs to the model
x1 = torch.randn(4,3,64,64)
