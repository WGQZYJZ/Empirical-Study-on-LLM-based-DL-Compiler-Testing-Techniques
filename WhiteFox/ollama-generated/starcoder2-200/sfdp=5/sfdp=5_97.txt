
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:  # 4 args
        attn = torch.softmax((query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1)), dim=-1)

        attn = torch.dropout(attn, dropout_p=0.5, training=self.training)

        output = attn @ value  # 3 args
        return output

# Initializing the model
m = Model()

