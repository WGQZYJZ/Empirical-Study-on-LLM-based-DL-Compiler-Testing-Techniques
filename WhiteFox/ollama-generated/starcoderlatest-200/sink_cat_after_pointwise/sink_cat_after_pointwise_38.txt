
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate the input tensor and the second tensor along axis 0
        v2 = v1.view(-1, 6)        # Reshape tensor into a vector
        v3 = torch.relu(v2)       # Apply ReLU function to v2
        return self.linear(v3)   # Pointwise operation applied on v3


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 5)
