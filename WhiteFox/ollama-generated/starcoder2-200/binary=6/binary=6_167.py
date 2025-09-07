
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        return (v7 - other) * 0.5


# Initializing the model
m = Model()
__other__ = torch.randn(3, 4).to("cuda:0") # Tensor to be subtracted from the output of linear transformation in the forward function
# Inputs to the model
x2 = torch.randn(16, 8)
