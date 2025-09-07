
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 - 7 # subtract a constant value from the output of the convolution
        v3  = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1   = torch.randn(4, 3, 80, 60) # input tensors to the model are randomly generated here. Please modify the model accordingly.

__output__  = m(x1)

