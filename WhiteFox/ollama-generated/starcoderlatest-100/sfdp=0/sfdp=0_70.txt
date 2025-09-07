
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.attention = torch.nn.Linear(dim * 2, dim)
 
    def forward(self, query, key, value, inv_scale):
        batch_size = query.shape[0]
        key = key.view(batch_size, -1, query.shape[-1])
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, dim: int, head_num: int, mlp_num: int, dropout: float):
        super().__init__()
        self.attention = ScaledDotProductAttention(dim=dim)
        self.dense1 = torch.nn.Sequential(
            torch.nn.Linear(dim, dim * 4),
            torch.nn.GELU(),
            torch.nn.Dropout(p=dropout),
        )
        self.dense2 = torch.nn.Sequential(
            torch.nn.Linear(dim * 4, mlp_num),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=dropout),
            torch.nn.Linear(mlp_num, dim),
        )
 
    def forward(self, query, key, value, inv_scale):
        output = self.attention(query, key, value, inv_scale)
        return self.dense2(torch.cat([output, query], dim=-1))
 

class TransformerEncoder(torch.nn.Module):
    def __init__(self, dim: int, head_num: int, mlp_num: int, dropout: float, num_layers: int):
        super().__init__()
        self.model = torch.nn.Sequential()
        for layer in range(num_layers):
            self.model.add_module("layer_" + str(layer), TransformerEncoderLayer(dim=dim, head_num=head_num, mlp_num=mlp_num, dropout=dropout))
 
    def forward(self, query, key, value, inv_scale):
        for layer in self.model:
            query = layer(query, key, value, inv_scale)
        return query


class Model(torch.nn.Module):
    def __init__(self, dim: int, head_num: int, mlp_num: int, dropout: float, num_layers: int):
        super().__init__()
        self.encoder = TransformerEncoder(dim=dim, head_num=head_num, mlp_num=mlp_num, dropout=dropout, num_layers=num_layers)
 
    def forward(self, query, key, value, inv_scale):
        return self.encoder(query, key, value, inv_scale)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
