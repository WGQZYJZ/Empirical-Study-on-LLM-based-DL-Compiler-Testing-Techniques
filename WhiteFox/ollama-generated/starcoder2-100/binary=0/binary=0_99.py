
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, other):
        v1  = self.conv(x1) + other 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__other__ = torch.randn(8,) 

 # Running the model and printing output
output_tensor   = m(x1, __other__)
print(output_tensor[0][0])

