
class Model(torch.nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.layer = torch.nn.LayerNorm(8)

        self.attn = torch.nn.Linear((num_heads * d_model), 1, bias=False)

    def forward(self, x):
        conv2d = self.conv1(x)
        attention = self.attn(conv2d).unsqueeze(-1)
        output = attention @ x
        return output


# Initializing the model
m = Model(8, 4)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
