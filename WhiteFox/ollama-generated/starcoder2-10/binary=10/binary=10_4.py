
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(3, 50).to("cuda:0") # Generating a random tensor to add 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
__inputs__ = torch.randn(47, 3)
