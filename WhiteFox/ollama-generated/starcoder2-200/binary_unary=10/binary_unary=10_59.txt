
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # another tensor (v1 is the output of the linear transformation in this example). Please note that "other" will be replaced with another tensor as input_tensor.
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model, a 10x3 matrix for the first input; and another 10x64 for the second input; other is another 5x1 tensor which can be generated randomly.
x1 = torch.randn(10, 3)
other = torch.randn(10, 5) # a random 10x5 matrix as the second input to the model.
