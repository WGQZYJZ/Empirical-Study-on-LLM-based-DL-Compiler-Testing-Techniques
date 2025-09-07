
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Inputs to the model
other = torch.tensor([0, 4]) # Define 'other' as a tensor containing zeros and one. 
x1 = torch.randn(1, 3)          # Generate an input tensor of dimension (1, 3). This tensor will be subtracted from the output of the linear transformation in `Model`.


