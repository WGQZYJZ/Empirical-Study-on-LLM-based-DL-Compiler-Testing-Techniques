
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(256, 1)
 
    def forward(self, x1, x2):
        v1 = x2 * torch.tanh(x1)
        a1 = self.attention(v1)
        attention_weights  = torch.nn.functional.softmax(a1, dim=-1)
        attention_weighted_values = x1 * attention_weights.unsqueeze(-1).expand_as(x1)
        return torch.sum(attention_weighted_values, dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
x2 = torch.randn(20, 8, 64, 64)
