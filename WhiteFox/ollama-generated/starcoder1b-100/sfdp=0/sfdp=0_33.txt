
class Model(torch.nn.Module):
    def __init__(self, num_layers=2, hidden_dim=16):
        super().__init__()
        self.num_layers = num_layers
        self.layer = torch.nn.Linear(hidden_dim, 8)
 
    def forward(self, x):
        for _ in range(self.num_layers - 1):
            output = self.layer(x)
            output = F.gelu(output)
            output = F.dropout(output, p=0.5)
            x = torch.cat((x, output), dim=-1)
        return x


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = x1 # A tensor of shape (B, C, H, W). Here `C = 3`, but this input can be any shape.
__output__  = m(input_tensor)


