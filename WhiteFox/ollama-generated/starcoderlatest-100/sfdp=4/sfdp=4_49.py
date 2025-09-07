
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 256)
        self.mlp = torch.nn.Sequential(
            torch.nn.LayerNorm(512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 2048),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(2048, 1024),
            torch.nn.LayerNorm(1024),
        )
        self.linear = torch.nn.Sequential(
            torch.nn.LayerNorm(1024 * 5),
            torch.nn.ReLU(),
            torch.nn.Linear(1024 * 5, 768),
        )
 
    def forward(self, x1):
        qk = x1 @ self.attn.weight.t() / math.sqrt(x1.size(-1)) + self.attn.bias
        qk = torch.softmax(qk, dim=-1) * (x1 != 0).type_as(qk) + 1e-8  # Apply the attention mask to the scaled dot product
        output = x1 @ qk.transpose(-2, -1) / math.sqrt(qk.size(-1))
        output = self.mlp(output).view(x1.size(0), -1, 512).mean(dim=1)
        output = self.linear(output) + x1[:, 0].unsqueeze(0)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 768, 512)
