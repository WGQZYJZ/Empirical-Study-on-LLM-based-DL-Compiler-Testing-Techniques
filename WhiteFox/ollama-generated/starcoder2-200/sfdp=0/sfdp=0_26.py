

class Attention(torch.nn.Module):
    def __init__(self, embedding_dim=768, num_heads=4, inv_scale=-10000):
        super().__init__()

        self.embedding_dim = embedding_dim
        self.num_heads    =  num_heads

        self.head_dim        =  embedding_dim //  num_heads
        assert self.head_dim *   num_heads == self.embedding_dim, "embedding dimensions must be divisible by number of heads"

        self.query       = torch.nn.Linear(self.embedding_dim,      self.embedding_dim)
        self.key         = torch.nn.Linear(self.embedding_dim, 3 *   self.head_dim ) 
        self.value       = torch.nn.Linear(3 *   self.head_dim , embedding_dim)

        self.scaled_dot_product_attention  = torch.nn.Sequential(
            torch.nn.Linear(self.embedding_dim,      self.embedding_dim), # query
            torch.nn.Softmax(),                         # attention
            torch.nn.Linear(self.embedding_dim, embedding_dim)  )       # value
 
        self.scale = (inv_scale == -10000) or inv_scale == None
        if   not     self.scale: assert isinstance(inv_scale , float),    "invalid scale"

        self.scaling_factor = inv_scale / math.sqrt(self.head_dim)
 
    def forward(self, query):
        Q  = self.query(query)
        KV= self.key(Q).view(-1, self.num_heads *  3 *   self.head_dim ).chunk(3, dim=-1)

        keys, values     , key_queries       = [torch.squeeze(a) for a in  KV]
        keys             , values           *=  self.scaling_factor
        value_norm       = torch.cat([values,keys], -2)
 
        attention_weights = self.scaled_dot_product_attention(key_queries)

        output = attention_weights @  values + key_queries
        return torch.split(output , self.head_dim, dim=-1 )

# Initializing the model
m = Attention()

