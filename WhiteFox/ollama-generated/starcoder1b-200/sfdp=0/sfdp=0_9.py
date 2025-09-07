
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        dot = self.conv(x1).view(-1, 3*8*8)  # Reshape to (B*N, 3*8*8)
        scale = torch.sqrt(torch.diag(dot).unsqueeze(-2).expand(dot.size()).unsqueeze(-2))  # Square root of diagonal elements of dot
        attention_weights = scaled_dot_product = dot / inv_scale
        output = attention_weights.matmul(value)  # Attention weights are multiplied with the value vector, and then summed
        return output


# Initializing the model
m = Model()


