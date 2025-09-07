
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, (64, 128), dim=0) # Return True if all of the splits in the input tensor are used in the concatenation operation.


# Input to the model
m = Model()
input_tensor = ...
