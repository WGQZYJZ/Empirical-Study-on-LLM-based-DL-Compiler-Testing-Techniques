
class Model(torch.nn.Module):
    def __init__(self, dim_model=64, vocab_size=128):
        super().__init__()
        self.fc = torch.nn.Linear(dim_model, vocab_size)
 
    def forward(self, x1, x2):
        query = self.fc(x1).view(-1, self.fc.in_features)
        key = self.fc(x2).transpose(-2, -1).contiguous().view(-1, self.fc.in_features)
        value = torch.mm(x1, x2.t()).div(self.fc.weight.size(-1) ** 0.5)
        attn_mask = (torch.arange(self.fc.out_features).expand(attn_p, -1) < attn_q).unsqueeze(-1)
        output = torch.bmm(query, key).div(math.sqrt(key.size(-1)))  # Batched dot product
        return torch.softmax(output, dim=-1), attn_mask


# Initializing the model
m = Model()

