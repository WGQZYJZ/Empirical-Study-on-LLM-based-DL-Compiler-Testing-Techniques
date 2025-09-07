
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 10)
 
    def forward(self, x1: Tensor):
        # linear transformation to the input
        v1 = self.linear(x1)

        # add another tensor to the output of the linear transformation
        # t2 is of type "Tensor"
        v2 = v1 + torch.randn(v1.shape)

        # apply relu activation function to the result
        return relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, requires_grad=True)
