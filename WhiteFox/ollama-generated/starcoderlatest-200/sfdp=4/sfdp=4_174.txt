
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(48, 512)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) # Query convolution
        v2 = x2 @ x2.transpose(-2, -1).contiguous() # Key convolution
        v3 = torch.cat([v1, v2], dim=-1) # Concatenate the two tensor by dimension 4
        v4 = torch.nn.ReLU()(self.linear(v3)) # Apply a non-linearity to the concatenated tensor and then reshape it
        v5 = self.conv(v4) # Value convolution
        return attn_weight @ value  # Compute the dot product of the attention weights and the value
# Initializing the model
m = Model()

