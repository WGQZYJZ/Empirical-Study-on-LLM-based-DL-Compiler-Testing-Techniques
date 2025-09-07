
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):

        # Input 2: permute the first dimension of the input tensor.

        v4 = torch.matmul(x1[0].permute(-1, -3), x1[-1])
        return [v4]


# Initializing the model
m = Model()

# Inputs to the model
__input_A_0__  = torch.randn(256) # Input Tensor 1. The first dimension is a dummy value.
x1  = torch.randn((7, 4))  # Input Tensor 3. Has two dimensions.
y1 = [torch.randn((7)),
      torch.randn((7))]  # List of 2 input tensors.
# __output__  = m(x1[0], y1)

