
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 64)
        self.key = torch.nn.Linear(64, 64)
 
    def forward(self, x1, x2):
        scale = torch.exp(self.query(x2).pow(2)).unsqueeze(-1) / \
            torch.sqrt((torch.exp(self.key(x1)) + 0.000001) *
                    (torch.exp(self.key(x2)) + 0.000001)).unsqueeze(-2)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


