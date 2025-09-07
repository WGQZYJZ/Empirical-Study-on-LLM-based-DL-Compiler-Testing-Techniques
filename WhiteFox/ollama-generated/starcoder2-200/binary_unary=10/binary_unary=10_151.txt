
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16 * 32 * 8, 9)

    def forward(self, x):
       x1 = x.view(-1, 16 * 32 * 8) # Reshape the input tensor to a 4d vector with batch size of 1 and 4d size of [16*32*8]
       v1 = self.linear(x1) + other_tensor  # Apply linear transformation to this vector, then add another tensor
       return torch.nn.functional.relu(v1).detach()


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(9)

x = torch.rand(4, 8 * 32 * 16)
__output__  = m(x)

