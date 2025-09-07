
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28 * 28, 30)
 
    def forward(self, x1):
        v1 = self.linear1(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + 0  # Add another tensor (in this case an all-zero tensor with the same size as `v1`) to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 784)
__output__= m(x1)