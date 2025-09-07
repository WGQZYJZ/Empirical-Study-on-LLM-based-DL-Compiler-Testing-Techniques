
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [4, 2], dim=0) # Split the input tensor along dimension 0 at position 1 (i.e., second) and dimension 0 at position 3 (i.e., fourth)
        concatenated_tensor = torch.cat(split_tensors, dim=0) # Concatenate split tensors along the same dimension
        return concatenated_tensor


# Initialization of the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
