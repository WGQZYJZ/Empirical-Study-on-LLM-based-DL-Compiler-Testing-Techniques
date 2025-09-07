
class TransformerBlock(nn.Module):
    def __init__(self, dim_q, dim_k, dim_v, num_heads=4, feedforward_dim=None, dropout_p=0., is_self_attention = True, attn_mask_mode='B', attn_dropout_p=0.):
        super().__init__()

        self.is_self_attention = is_self_attention
        assert dim_k % num_heads == 0 and dim_v % num_heads == 0
        if feedforward_dim:
            ffn = nn.Sequential(
                nn.Linear(feedforward_dim, feedforward_dim), 
                nn.ReLU(),
                nn.Dropout(dropout_p)
                )
            
        self.attn_mask_mode = attn_mask_mode
        if self.attn_mask_mode=='A':
            # generate attention mask based on query size and key size
            assert dim_q > dim_k, 'The dimension of query should be greater than the key'
            num_attn_heads = 1 + (dim_q-dim_k)//(dim_k//num_heads) 
            attn_mask_tensor = torch.zeros((num_attn_heads, num_attn_heads, dim_q+dim_k))
            if is_self_attention:
                k_pad = int(0.1*dim_k) # padding for kernel size in attention mechanism
                q_pad = int(0.1*dim_q) 
                attn_mask_tensor[0][:,-attn_mask_mode][-q_pad:] = 1
            self.attn_mask = nn.Parameter(attn_mask_tensor, requires_grad=False).cuda()
        else:
            self.attn_mask = None

        if is_self_attention:
            assert dim_k == dim_v, 'The dimension of key and value should be the same'
            
            self.q = nn.Linear(dim_q, num_heads*dim_k) # num_heads * k
            self.key = nn.Linear(dim_k, num_heads*dim_k)
            self.v = nn.Linear(dim_v, num_heads*dim_v) 
            
            attn_dropout_layer = torch.nn.Dropout(attn_dropout_p)
        else:
            assert dim_q == dim_k and feedforward_dim is None
            # add a linear transformation to each output of the transformer
            self.w1 = nn.Linear(dim_q, num_heads*dim_v)
            self.w2 = nn.Linear(dim_k, num_heads*dim_v)
            attn_dropout_layer = torch.nn.Dropout(attn_dropout_p)
        # feedforward network is only applied to the last transformer block
        self.feedforward = ffn if feedforward_dim else None
        self.attn_dropout = attn_dropout_layer

        self.softmax = nn.Softmax(-1)
        
        self._initialize()
 
    def _initialize(self):
        init.xavier_uniform_(self.q.weight, gain=nn.init.calculate_gain('linear'))
        init.constant_(self.v.bias, 0.)

    # forward function
    def forward(self, query, key, value):

        if self.attn_mask:
            q_pad = int(0.1*query.shape[-1]) 
            attn_mask = self.attn_mask[:1,:,-q_pad:]
        else:
            attn_mask = None

        # linear transformation for all the input tensors
        w1 = self.w1(query) 
        if isinstance(w1, tuple):
            w1, _ = w1
            dim_v, num_heads = dim_v.contiguous(), num_heads.contiguous()

        qk = torch.matmul(self.q(query), self.key(key.transpose(-2,-1))) # batch_size * dim_q * num_heads * dim_k
        if isinstance(qk, tuple):
            attn_weight, _ = qk
        else:
            attn_weight = F.softmax(qk/math.sqrt(query.shape[-1]), dim=-1) # apply softmax to the scaled dot product
        attn_weight = self.attn_dropout(attn_weight)

        # linear transformation for each output of attention mechanism
        w2 = torch.matmul(self.w2(key), self.v(value)) 
        if isinstance(w2, tuple):
            v_new, _ = w2
        else:
            v_new = F.linear(key, value)

        # scale dot product and add the attention mask
        attn_weight = torch.unsqueeze(attn_weight, dim=-1) * attn_mask
        
        # compute output of attention mechanism
        output = attn_weight @ v_new 

        if isinstance(output, tuple):
            output, _ = output

        # feedforward network: apply a linear transformation to the output of attention mechanism (v_new), and then relu, and then apply dropout
        if self.feedforward is not None:
            output = self.feedforward(output) 

        return output
class Model(torch.nn.Module):
    def __init__(self, num_layers=2):
        super().__init__()
        self.num_blocks = num_layers 
        self._initialize()

    # forward function
    def forward(self, x1, x2):

        for i in range(self.num_blocks):
            ffn = nn.Sequential(
                nn 
            if __ __
    else: You have an invalid device type)
def _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _