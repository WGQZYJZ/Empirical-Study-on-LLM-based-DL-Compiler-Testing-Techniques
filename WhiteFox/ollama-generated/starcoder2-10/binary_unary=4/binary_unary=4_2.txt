
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1): 
        v0 = torch.tensor([5], device="cuda") # Initialize a constant tensor with the value 5 and place it on GPU (CUDA) memory
        v2 = self.linear(x1, other=v0) # Apply a linear transformation to the input tensor; then add another tensor of constant values to the result 
        return torch.relu(v2 + x3)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 64).cuda() # Generate an input tensor for the model on GPU (CUDA) memory that is of size 1 × 64
__output__  = m(x1)


