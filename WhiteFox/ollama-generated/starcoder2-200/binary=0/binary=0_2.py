
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.other = other

    def forward(self, x1):
       v1  = self.conv(x1) + self.other
       return v1

# Initializing the model
m  = Model()

 # Inputs to the model: Two input tensors with different shapes. The "other" tensor should be broadcastable and of the same type as other_tensor, and be a keyword argument for the addition operation in the forward method.
input0  = torch.randn(1,3,64,64)
input1  = torch.randn(2,8,79,57)
__output__  = m(input0, other=input1)


