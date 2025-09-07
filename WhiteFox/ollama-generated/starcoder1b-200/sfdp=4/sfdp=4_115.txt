
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 8)
        self.ln1 = nn.LayerNorm([32, 32])
 
    def forward(self, x1):
        v1 = self.attn(x1).transpose(-2, -1)  # Get the attention weights
        v2 = torch.nn.functional.layer_norm(x1, x1.size()[:-1]) * 0.5  # Apply pointwise convolution to the input tensor
        v3 = torch.nn.functional.layer_norm(v2, x1.size()[:-1]) * 0.7071067811865476  # Multiply the output of the first convolution by the constant
        v4 = torch.erf(v3) + 1
        v5 = v2 * v4
        return v5


# Initializing the model
m  = Model()


