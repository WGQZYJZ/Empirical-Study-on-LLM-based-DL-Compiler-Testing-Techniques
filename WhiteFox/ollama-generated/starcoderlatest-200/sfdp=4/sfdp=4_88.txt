
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = torch.nn.Parameter(data=torch.Tensor([[1, 0], [0, -2]]), requires_grad=True)
 
    def forward(self, query, key, value):
        attn_weight = self.attn_weight * torch.softmax((query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)), dim=-1) + 1e-9
        return attn_weight @ value
 
# Input tensors to the model
query = torch.randn(16, 512, 100)
key = torch.randn(32, 512, 100)
value = torch.randn(16, 512, 100)
 
# Forward computation of the model with the given input tensors
attn_weights = m(query, key, value)


