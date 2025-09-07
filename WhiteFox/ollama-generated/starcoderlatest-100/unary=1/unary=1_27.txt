
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3*64*64, 512) # [in_features] = [3 * width of each image] * [height of each image] * [channels in the model] = (3 * 64) * 64 * 3
        self.linear2 = torch.nn.Linear(512, 512) # [in_features] = (512)
        self.linear3 = torch.nn.Linear(512, 32) # [in_features] = (512)
 
    def forward(self, x):
        v1 = self.linear1(x) # Apply linear transformation to the input tensor
        v2 = v1 * 0.5
        v3 = v1 + (v1 * v1 * v1) * 0.044715
        v4 = v3 * 0.7978845608028654
        v5 = torch.tanh(v4) # Apply the hyperbolic tangent function to the output of the previous operation
        v6 = v5 + 1 # Add 1 to the output of the hyperbolic tangent function
        v7 = v2 * v6 # Multiply the output of the linear transformation by the output of the hyperbolic tangent function
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3*64*64)
