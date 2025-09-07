
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[1024]):
        super().__init__()
 
    def forward(self, x):
        torch.split(x) # Split an input tensor into several tensors along the first dimension using `torch.split`
        torch.cat([None], dim=0))  # Concatenate a list of tensors along their first dimension using `torch.cat`. The list contains one None argument.
        return x

# Initializing and testing
m = Model(split_sizes=[1,5]) # Initialize the model with an input size equal to [1, 5] along the 0th axis for demonstration purposes
x = torch.randn(12) # Generate a tensor of 12 elements that will be used as input to the model during testing
__output__  = m(x)

