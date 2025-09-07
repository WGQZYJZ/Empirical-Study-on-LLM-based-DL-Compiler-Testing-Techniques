
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model and setting `other`
m = Model()
other  = torch.randn(32*64*64, 10).requires_grad_()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)


__output__  = m(x1), other # Returns the model output and `other` tensor as outputs