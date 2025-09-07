
class Model(torch.nn.Module):
    def __init__(self, inv_scale: float = 0.1):
        super().__init__()
        self.linear1 = torch.nn.Linear(768 * 4 * 4, 3072)
        self.linear2 = torch.nn.Linear(3072, 768 * 4 * 4)
        self.inv_scale = inv_scale
 
    def forward(self, x1, x2):
        t1 = F.relu(self.linear1(x1.view(-1, 768 * 4 * 4)))
        t2 = F.relu(self.linear2(t1.view(-1, 3072)))
        scaled_dot_product = torch.matmul(t2, t1.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Inputs to the model
query  = torch.randn(2, 8, 64, 64)
key    = torch.randn(2, 8, 32, 32)
inv_scale = torch.sqrt(torch.tensor([1.0 / (256 * 256)]))
x1 = key.transpose(-2, -1).unsqueeze(-2)
x2 = query.unsqueeze(-1)


# Initializing the model and its parameters with a specific `inv_scale`
m = Model(inv_scale=inv_scale)
params = m.parameters()
for p in params:
    print('param size:', p.size())
print('')

# Inputs to the model
