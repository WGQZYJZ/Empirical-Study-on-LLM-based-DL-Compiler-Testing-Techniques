
class Model(torch.nn.Module):
    def __init__(self, key_dim, value_dim, dropout_p=0.3):
        super().__init__()
        self.key_dim = key_dim
        self.value_dim = value_dim
        self.dropout_p = dropout_p
        self.query = torch.nn.Parameter(torch.randn(1, self.key_dim)), requires_grad=True)
        self.key = torch.nn.Parameter(torch.randn(1, self.value_dim)), requires_grad=True)
        self.scale = torch.sqrt(self.value_dim * key_dim)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x):
        scaled_query  = self.query.mul(self.scale)
        dropout_query = torch.nn.functional.dropout(scaled_query, p=self.dropout_p)
        dot_product = dropout_query.matmul(self.key)
        output = self.softmax(dot_product).matmul(x)
        return output


# Initializing the model
model = Model(key_dim=32, value_dim=64)

