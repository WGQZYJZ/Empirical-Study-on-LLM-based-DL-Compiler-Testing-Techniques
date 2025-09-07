
class Model(torch.nn.Module):
    def __init__(self, num_layers=12, embed_size=2048):
        super().__init__()
        self.attn = torch.nn.Linear(embed_size, embed_size, bias=True)
        self.fc  = torch.nn.Linear(embed_size * 3, embed_size)
        self.layers = []

        for i in range(num_layers):
            layer = torch.nn.TransformerEncoderLayer(d_model=embed_size, nhead=2, dim_feedforward=embed_size // 4, dropout=0.1)
            self.add_module('layer{}'.format(i + 1), layer)

        self.output = torch.nn.Linear(embed_size, embed_size, bias=True)
 
    def forward(self, x):
        x = self.attn(x)  # The first layer computes the dot product of the query and key (plus an attention mask)
        for i in range(2, len(self.layers)):
            x = torch.relu(self.layers[i - 1](x))

        x = self.fc(torch.relu(self.output(x)))
        return x


# Initializing the model
m = Model()


