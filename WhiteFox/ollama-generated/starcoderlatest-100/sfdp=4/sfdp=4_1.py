
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 1024)
        self.key = torch.nn.Linear(768, 1024)
        self.value = torch.nn.Linear(768, 1024)
        self.attention_mask = torch.nn.Parameter(torch.zeros(1, 3, 64, 64))

    def forward(self, x):
        qk = (x @ self.query.weight.t()) / math.sqrt(x.size(-1)) + self.attention_mask
        attn_weights = torch.softmax(qk, dim=-1)
        output = (attn_weights * self.value.weight).sum(dim=0)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(5, 3, 768)
