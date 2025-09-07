
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.tensor([[0, 1], [2, 3]])
 
    def forward(self, x):
        y = torch.full([x.shape[0]], 0, dtype=torch.long, layout=torch.strided)
        return y


# Inputs to the model
x  = torch.randn(4)  # Create a tensor filled with a normal distribution of standard normal random numbers
y  = torch.full([x.shape[0]], 1, dtype=torch.long, layout=torch.strided)  # Fill the tensor with all-ones values
