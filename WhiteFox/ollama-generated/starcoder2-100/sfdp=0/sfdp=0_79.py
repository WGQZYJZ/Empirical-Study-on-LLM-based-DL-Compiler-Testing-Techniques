
class Attention(nn.Module):
    def __init__(self, d_model: int = 512):
        super().__init__()
 
        self.d_model = d_model
        inv_scale = torch.ones(()) / (d_model ** -0.5)
        self.softmax = nn.Softmax(dim=-1)
 
        self._query = nn.Linear(
            in_features=d_model, out_features=d_model, bias=False)
        self._key = nn.Linear(
            in_features=d_model, out_features=d_model, bias=False)
 
        self._value = nn.Linear(in_features=d_model,
                                out_features=d_model, bias=False)
        self.scale = torch.nn.Parameter(data=inv_scale, requires_grad=True)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):
 
        q = self._query(query).view(*query.shape[:-1], -1)
        k = self._key(key).view(*key.shape[:-1], -1)
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / (
            self.d_model ** -0.5)
 
        attention_weights  = self.softmax(scaled_dot_product)

        return self._value(attention_weights).view(*key.shape[:-1],
                                                    *query.shape[-2:])
 

# Initializing the model
att = Attention()


# Inputs to the model
query = torch.randn([8, 3, 64])
 
key = torch.randn([8, 3, 64])

__output__  = att(query, key)

