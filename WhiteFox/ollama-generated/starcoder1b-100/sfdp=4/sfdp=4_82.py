
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(32, 32)
        self.key    = torch.nn.Linear(32, 32)
        self.value  = torch.nn.Linear(32, 16)

    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        v = torch.bmm(v1.transpose(-2, -1), v2) / math.sqrt(v1.size(-1))
        w1 = torch.softmax(v1, dim=-1).unsqueeze(0)  # Compute the attention weights as softmax(v1), where 0 is added to the result because we are using softmax here
        return self.value(w1 @ v)  # Compute output of the linear layer


# Initializing the model
m = Model()


