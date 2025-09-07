
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate the two input tensors along a dimension (dimension 0 in this example). 
        v2 = v1.view(-1, x1.size()[1]*x2.size()[1]) # Reshape tensor to [batch_size*input_dim]
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2) # Input tensor 0: x1, x2
x2 = torch.randn(1, 2, 4) # Input tensor 1: x3
