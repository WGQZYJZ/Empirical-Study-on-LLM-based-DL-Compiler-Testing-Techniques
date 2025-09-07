
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(128, 10, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
        v1 = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the scaled dot product of the query and key tensors, and scale it
        v1 = v1 + torch.eye(v1.shape[-1]).to(device) * 0.1 # Add the attention mask to the scaled dot product, set all weights to be approximately equal in magnitude with their respective value (i.e., 0.1 for the diagonal).
        v2 = torch.softmax(v1, dim=-1) # Apply softmax to the result
        output = v2 @ x1 # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 64, 64)  # input tensor for q
x2 = torch.randn(5, 32, 64)  # input tensor for k
