
class Attn(nn.Module):
    def __init__(self,
                 in_dim: int,
                 out_dim: int = None,
                 key_proj_out=128,  # this parameter is not used for model generation purpose; it just serves as a way to specify the number of outputs after applying the projection layer.
                 query_hidden_size=None):
        super(Attn, self).__init__()
 
        self.query_layer = nn.Linear(in_dim if query_hidden_size is None else query_hidden_size, in_dim)
        self.key_layer = nn.Linear(2 * in_dim, 160)  # this parameter is not used for model generation purpose; it just serves as a way to specify the number of outputs after applying the projection layer.
 
        self.value_layer = nn.Linear(in_dim, out_dim if query_hidden_size else in_dim)
 
    def forward(self,
                input: torch.Tensor,
                memory: torch.Tensor):
        q_mem_query = torch.cat((memory,
                                 self.key_layer(
                                     self.query_layer(input))), dim=-1).transpose(-2,-1)
        # Compute the dot product of the query and key matrices.
        v = (torch.softmax(q_mem_query + self.key_layer(self.query_layer(memory)), 
                           dim=0) * self.value_layer(input)).sum(dim=-2,keepdims=True).expand(-1,-1,self.value_layer(memory).shape[-1])
 
        return v
