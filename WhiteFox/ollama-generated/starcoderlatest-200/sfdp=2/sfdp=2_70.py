
class Model(torch.nn.Module):
    def __init__(self, embed_dim, head_num=8, dim_feedforward=2048):
        super().__init__()
        self.layer_norm_embed = torch.nn.LayerNorm([1])
        self.embedding = torch.nn.Embedding(vocab_size, embed_dim)
 
        # Create 3 heads for attention and create the attention layer
        head = torch.nn.Linear(2 * embed_dim, dim_feedforward)
        self.attention = torch.nn.ModuleList([torch.nn.Linear(embed_dim, dim_feedforward),
                                             torch.nn.Linear(embed_dim, dim_feedforward)])
 
        # Create 3 heads for position-wise Feed Forward Network and create the FFN layer
        feed_forward = torch.nn.Sequential(
            torch.nn.Linear(2 * dim_feedforward, dim_feedforward),
            torch.nn.ReLU(),
            torch.nn.Linear(dim_feedforward, embed_dim),
        )
        self.ffn = torch.nn.ModuleList([feed_forward for _ in range(3)])
 
        # Create 1 heads and create the layer normalization and the final layer
        linear = torch.nn.Linear(2 * embed_dim + dim_feedforward, 512)
        self.layer_norm_output = torch.nn.LayerNorm([512])
        self.linear = torch.nn.Sequential(
            torch.nn.Linear(embed_dim, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, embed_dim),
        )
 
        self.layer_norm_final = torch.nn.LayerNorm([vocab_size])
 
    def forward(self, x):
        x = self.embedding(x)
        x = self.layer_norm_embed(x + [0])
        y1, y2, z = [], [], []
 
        for i in range(3):
            # Forward Pass of the 4 layers (i == 0: query, i == 1: key; i == 2: value)
            h1 = self.attention[i](x).relu()
            h2 = self.ffn[i](h1)
            y1.append(h1), y2.append(h2), z.append(h2 + x)
 
            # Compute the final output of the 4 layers, and combine the outputs of all 4 layers together (along with the input) into a single tensor
            if i == 0:
                h3 = self.layer_norm_final(torch.cat(y1, dim=-2))
            else:
                h3 = self.layer_norm_output(torch.cat([x] + y1, dim=-2))
        x = torch.cat(z, dim=-2)  # Combine the outputs of the 4 layers along with the input tensor into a single tensor
 
        x = self.linear(h3).relu()
        return x
 
 # Initializing the model
m = Model(512)
 
 # Inputs to the model
x1 = torch.randint(0, vocab_size - 1, (64,))
