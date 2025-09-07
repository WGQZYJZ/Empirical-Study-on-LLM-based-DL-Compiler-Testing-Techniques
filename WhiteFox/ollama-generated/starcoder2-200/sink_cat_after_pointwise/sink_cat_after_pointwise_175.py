
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.cat([x2, x3], dim=0)  # Concatenate tensors along a dimension
        v4 = v3.view(-1, 50).view(20, -1)

        v7 = torch.nn.functional.relu(v4) # Apply ReLU to the reshaped tensor
        return v7


# Initializing model
m = Model()
# Inputs to the model
x2 = torch.randn(5, 6).cuda() + x1
x3 = torch.randn(10, 6).cuda() + x1
