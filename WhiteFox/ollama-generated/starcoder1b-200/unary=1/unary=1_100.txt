
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x):
        v = self.linear(x).view(x.size()[0], -1)  # Reshape the input tensor to match the output of the linear transformation (View).
        v = v * 0.5
        v = torch.cat([v, v, v], dim=1) + 0.044715  # Add the output of the previous operation with an additional scalar to the output of the linear transformation cubed multiplied by `0.044715`.
        v = v * 0.7978845608028654
        v = torch.tanh(v) + 1
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3, 28, 28)
