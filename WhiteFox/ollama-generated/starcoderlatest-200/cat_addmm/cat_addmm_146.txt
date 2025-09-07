
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 1)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, dim=1) # Add a matrix multiplication between two tensors with an additional dimension of size one to the input tensor
        v2 = torch.cat([v1], dim=1) # Concatenate this result along the final axis (axis 1)
        return v2
 

# Initializing the model
m = Model()


x1 = torch.randn(1, 8)
x2 = torch.randn(1, 4)
