
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 24)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor  # Applying linear transformation and adding another tensor to the output of the linear transformation
        v2 = v1 + torch.relu(v1)             # Applying ReLU activation function to the result of adding anohter tensor to the output of the linear transformation
        return v2


# Initializing the model