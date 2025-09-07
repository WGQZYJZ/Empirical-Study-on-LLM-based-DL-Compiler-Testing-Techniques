
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
       v1  = self.conv(x1)
       return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)

# The second argument for convolution operator is kernel size
out_first = m(x1, 5)
out2 = m(torch.ones(10))

# In this case we expect that out[second_call] and out[first call are different

