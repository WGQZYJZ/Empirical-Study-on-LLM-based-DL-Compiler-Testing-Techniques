
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        t2 = torch.cat([t1, t1], dim=0)  # Concatenate tensors along a dimension
        t3 = t2.view(-1, 4)              # Reshape the concatenated tensor
        t4 = torch.nn.functional.relu(t3) # Apply ReLU to the reshaped and concatenated tensor
        return t4


# Initializing the model
m = Model()

# Inputs to the model
t1  = torch.randn(2, 2)
__output__  = m(t1)