
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=1) # Concatenate tensors along dimension 1
        v2 = self.relu(v1.view(-1, 4)) # Reshape the tensor and apply relu on the reshaped tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 2)
