
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, num_layer=4):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.num_layer = num_layer

        self.fc_proj  = torch.nn.Linear(d_model, d_model)
        self.layers = nn.ModuleList([
            SelfAttentionLayer(d_model, nhead, dropout=dropout_p)
            for _ in range(num_layer)])

    def forward(self, x):
        # (batch, seq_len, input_dim)
        hidden  = self.fc_proj(x)  # Input projection to the last fc layer
        output = []
        for i in range(self.num_layer):
            output.append(self.layers[i](hidden))

        return torch.cat(output, dim=1)


# Initializing the model
m = Model()
x  = torch.randn(2, 50, d_model)
