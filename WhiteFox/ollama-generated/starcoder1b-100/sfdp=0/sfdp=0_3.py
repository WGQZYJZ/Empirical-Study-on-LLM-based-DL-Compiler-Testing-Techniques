
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(32, 16)
        self.k = torch.nn.Linear(8, 4)
        self.v = torch.nn.Linear(16, 2)

    def forward(self, x1, x2):
        q = self.q(x1)
        k = self.k(x2)
        v = self.v(x2)
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(torch.FloatTensor([self.embedding_dim])).unsqueeze(-1)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output


# Inputs to the model
x1 = torch.randn(2, 32, requires_grad=True)
x2 = torch.randn(2, 8, requires_grad=True)
