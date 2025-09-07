
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 15)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v1 += other
        v3  = F.relu(v1) # Apply ReLU to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20, 50, 48).mean(axis=1, keepdims=True) # Input tensor with the shape (num_batches, batch_size, input_dimensionality) for a linear transformation layer
other = torch.randn(3978760, 50, 27) # Other tensor to be added to the output of the linear transformation
 
