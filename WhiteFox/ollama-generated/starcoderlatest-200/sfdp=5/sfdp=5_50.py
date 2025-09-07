
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model: int = 128, d_ff: int = 4096):
        super().__init__()
        self.d_model = d_model
        self.norm = torch.nn.LayerNorm(d_model)
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v1 = self.norm(v1)
        v1 = torch.relu(v1)
 
        # Add code that implements the TransformerEncoder block.
        return output

# Initializing the model
m = TransformerModel()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
