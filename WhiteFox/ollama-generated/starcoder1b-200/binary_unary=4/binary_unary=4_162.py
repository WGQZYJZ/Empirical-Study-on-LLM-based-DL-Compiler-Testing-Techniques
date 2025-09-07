
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)
 
    def forward(self, x1: torch.Tensor):
        v1  = self.linear(x1) + 5 # Add another tensor to the output of the linear transformation
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, requires_grad=True)
