
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 8, bias=False)
        self.key   = torch.nn.Linear(5, 16, bias=False)
        self.value = torch.nn.Linear(8, 256, bias=False)
 
    def forward(self, x1, x2):
        qk = self.query(x1).unsqueeze(-2) @ self.key(x2).transpose(-2, -1) / math.sqrt(torch.div(self.query.size(-2), 2))
        attn_mask = torch.triu(torch.ones((qk.shape[0], kq.shape[0]))) + torch.tril(torch.ones((qk.shape[1], kq.shape[1]))).cuda()
        attn_weight = F.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ self.value(x2)  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(3, 5, 10), torch.randn(3, 8, 20)
