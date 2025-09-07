
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other_tensor # Subtract 'other' from the output of the convolution 
        return v2


# Initializing the model with different inputs to test if it generates different code each time. 
m  = Model()
for i in range (0, 3):
    input_tensor1  = torch.randn(i + 1 , 3, 64, 64)
    __output__     = m(input_tensor1)

