
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv1(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp(v1, min_value=0.35786497075561667)  # Clamp the output of the previous operation to 0.35786497075561667
        v3 = torch.clamp(v2, max_value=0.9012286035075847)  # Clamp the output of the previous operation to 0.9012286035075847
        return v3

# Initializing the model
m = Model()


# Inputs to the model