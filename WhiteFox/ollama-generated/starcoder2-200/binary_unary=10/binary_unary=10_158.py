
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072 * 8, 4)
 
    def forward(self, x1): 
        v1 = self.linear(x1).reshape((8, -1))
        v2 = v1 + other # Add another tensor to the output of linear transformation
        v3 = torch.relu(v2) # Apply ReLU activation function to the result
        return v3
# Initializing the model
m  = Model()
 
other = torch.randn(8,4)# Input tensor


# Inputs to the model
x1 = other * np.array(3072)


