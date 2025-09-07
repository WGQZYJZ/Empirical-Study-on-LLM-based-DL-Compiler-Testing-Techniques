
class Attn(torch.nn.Module):
    def __init__(self, in_features, out_features, dropout=0., bias=False):
        super().__init__()
 
        self.query  = torch.nn.Linear(in_features, out_features)
        self.key  = torch.nn.Linear(in_features, out_features)
        self.value  = torch.nn.Linear(in_features, out_features)

        self.dropout = torch.nn.Dropout(p=dropout)
        if bias:
            self.bias  = torch.nn.Parameter(torch.zeros((out_features)))

    def forward(self, query):
 
        k = self.key(query).transpose(-2, -1)
        v = self.value(query)

        attn_mask  = (k == float('inf')).type_as(v)
        kq = torch.nn.functional.normalize(torch.bmm(self.dropout(self.query(query)), k), dim=-2)
        attn_weight  = torch.softmax(kq, dim=-1)
        output = torch.matmul(attn_weight, v)
        if self.bias is not None:
            output += self.bias
 
        return output

# Initializing the model
m  = Attn(4, 5)

