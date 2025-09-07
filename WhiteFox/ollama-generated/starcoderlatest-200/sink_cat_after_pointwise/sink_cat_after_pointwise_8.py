
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 5)

    def forward(self, x1):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along the dimension with size (2, 2)

        # Reshape tensor to match its dimension after concatenation to (6, 2)
        t2 = t1.view(-1, self.linear1.in_features) 
        
        # Apply pointwise operation (ReLU or Tanh) to reshaped tensor to make it compatible with linear function
        t3 = torch.nn.functional.relu(t2)

        # Apply linear transformation and return result. The weight of the linear transformation is obtained from the input tensor t1 
        v = torch.nn.functional.linear(t1, self.linear1.weight, self.linear1.bias)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4)
x2 = torch.randn(2, 3)
