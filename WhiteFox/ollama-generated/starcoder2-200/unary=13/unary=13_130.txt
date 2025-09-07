
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(64*64*8, 10)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution to the input tensor
        v2  = v1 * 0.5      # Multiply the output of the convolution by a constant `0.5`
        v3  = v1 * 0.7071067811865476   # Multiply the output of the convolution by another constant `0.7071067811865476` 
        v4  = torch.erf(v3) + 1    # Apply error function to the output of the convolution, and then add 1
        v5  = self.linear(torch.flatten(x1))
        v6  = sigmoid(t2) * t5   # Multiply the output of the sigmoid function by the output of the linear transformation
        return v6


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 __output__  = m(x1)
