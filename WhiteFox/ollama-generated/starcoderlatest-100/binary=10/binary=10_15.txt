
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.size()[0], -1)) # A linear transformation is applied to an input tensor and the resulting output is then flattened as an (n, d_out) tensor for the purpose of adding another tensor to it
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
