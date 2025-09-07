
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.ones(1, 32))
        self.key = torch.nn.Parameter(torch.ones(8000, 32))
        self.value = torch.nn.Parameter(torch.ones(79504, 64))
 
    def forward(self):
         vq_shape = tuple((v + 1) * [i for i in self.query.size() if not isinstance(i, int)])[:-1] + [-2]
         vk_shape = tuple((v + 1) * [i for i in self.key.size() if not isinstance(i, int)])[:-1] + [self.value.size(-3)]
         vv_shape = tuple([1]) + vq_shape
         qk = torch.nn.functional.linear(self.query, self.key) / math.sqrt(self.query.size(-2))
        attn_mask  = torch.ones((1,) + vv_shape) - torch.triu(torch.ones(1,) + vv_shape).type_as(qk)
        qk += attn_mask
         attn_weight  = torch.nn.functional.softmax(qk, dim=-2)
         attn_weight = torch.dropout(attn_weight, p=0.5, training=self.training)
         output = torch.nn.functional.linear(attn_weight @ self.value, bias=None if self.value.dim() > 3 else self.value[-1])
         return qk
 
# Initialize the model and run it
m  = Model()
__output__  = m()

