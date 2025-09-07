
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v1 = torch.nn.functional.linear(x1, self.linear.weight)
        v2  = v1.permute(0, 2, 1) # Permute the output of linear transformation to the input of permute method.
        return v2


# Initializing model
m  = Model()

# Input tensor for the model
x1 = torch.randn(4,)