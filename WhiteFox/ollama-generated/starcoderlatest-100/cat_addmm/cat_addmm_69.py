
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(64, 8) # Create a tensor of shape (num_input_features, num_output_features) filled with random numbers between -0.5 and 0.5
        self.mat2 = torch.randn(8, 3) # Create a tensor of shape (num_output_features, num_input_features) filled with random numbers between -0.5 and 0.5
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=1) # Concatenate the result along a dimension with index 1 (i.e. axis equals to 1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64, 64)
