
class EncoderLayer(torch.nn.Module):
    def __init__(self, n_head=4):
        super().__init__()
        self.layernorm1 = torch.nn.LayerNorm(10)
        self.layernorm2 = torch.nn.LayerNorm(53)
        self.ff = nn.Sequential(
            nn.Linear(786),  # 53 * 4 + 10
            nn.ReLU(),
            nn.Linear(786, 900))
 
    def forward(self, x):
        residual = x
        x += self.layernorm1(x)
 
        for layer in self.ff:
            x = layer(x)
            output += residual
 
        output /= math.sqrt(output.size(-1))  # Scale the result by a factor of sqrt(dimension)
        return output
