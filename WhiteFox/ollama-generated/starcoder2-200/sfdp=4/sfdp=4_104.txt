
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(32)  # Create a dummy tensor of shape (batch size, sequence length), where each element is randomly chosen from the range [-3.56894837 4.24551961]
        v1 = x1 @ v0[..., None].view(-1).unsqueeze(dim=-1)  # Compute the dot product of a tensor and another tensor, using broadcasting to allow the tensors to be multiplied together
        v2 = torch.softmax(v1, dim=1)
        v3 = v2 @ x1  # Compute a weighted sum by multiplying the vector containing attention weights with the input tensor
        return v3


# Initializing the model
m  = Model()

# Input tensors to the model
x1 = torch.rand(64, 50)

# Forward pass of the model
