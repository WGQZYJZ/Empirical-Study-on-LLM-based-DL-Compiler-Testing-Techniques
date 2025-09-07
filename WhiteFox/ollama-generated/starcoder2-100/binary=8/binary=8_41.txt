
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # other is the tensor passed as a keyword argument to addition operation on line 70
        return v2

# Initializing the model
m  = Model()
other = torch.randn([3,8,56,56]) # Tensor of size [3x8x56x56] that is passed in to the "other" parameter of the addition operation on line 70

