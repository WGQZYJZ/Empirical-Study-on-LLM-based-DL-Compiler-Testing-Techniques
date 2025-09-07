
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = torch.cat([x1, x2], dim=0)
        t2  = t1.view(-1, 5).clone().detach() # Reshape the concatenated tensor
        return torch.nn.functional.relu(t2[:, 3])


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4)
x2 = torch.randn(6, 5).clone().detach() # Generate a random tensor with the same shape as the previous input tensors x2
