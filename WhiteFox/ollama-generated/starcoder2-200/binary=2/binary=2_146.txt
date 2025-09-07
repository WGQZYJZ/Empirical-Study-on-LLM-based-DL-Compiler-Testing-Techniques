
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor) -> None:
        super().__init__()
        self.other = other

        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - self.other # Subtract 'other' from the output of the convolution
        return v2


# Initializing the model with other
m  = Model(torch.randn([3])) 

# Inputs to the model
x  = torch.randn([4, 3, 64, 64])
