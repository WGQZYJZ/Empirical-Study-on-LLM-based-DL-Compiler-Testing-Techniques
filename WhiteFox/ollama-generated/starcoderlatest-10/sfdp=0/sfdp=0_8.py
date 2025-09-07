
class MultiheadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = torch.nn.Dropout(p=dropout)
        self.linears = torch.nn.ModuleList([torch.nn.Linear(self.embed_dim, self.embed_dim) for _ in range(self.num_heads)])
        self.attn = None
 
    def forward(self, x):
        x = self._forward_layer(x, 0)
        x = self._forward_layer(x, 1)
        x = self._forward_layer(x, 2)
        return x
 
    def _forward_layer(self, x, layer_idx):
        # Linear layers and dropout
        for idx, lin in enumerate(self.linears[layer_idx]):
            x = torch.relu(lin(x))
            if idx != self.num_heads - 1:
                x = self.dropout(x)
 
        # Attention
        # (batch_size, query_len, key_len) * (query_len, embed_dim, num_heads) -> (batch_size, query_len, num_heads)
        att_score = torch.matmul(x, x.transpose(-2, -1))  # [N, Lq, Nk] * [Nk, D, H] -> [N, Lq, H]
 
        if self.attn is None:
            self.attn = MultiHeadAttention(embed_dim=self.embed_dim, num_heads=self.num_heads)
 
        # Attention weights (batch_size, query_len, num_heads)
        att_weights = self.attn(att_score).transpose(-2, -1)  # [N, Lq, H] * [H, Nk, D] -> [N, Lq, Nk]
        return att_weights


class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout = torch.nn.Dropout(p=dropout)
        self.attn = None
 
    def forward(self, x):
        x = self._forward_layer(x, 0)
        x = self._forward_layer(x, 1)
        return x
 
    def _forward_layer(self, x, layer_idx):
        # Linear layers and dropout
        for idx, lin in enumerate(self.linears[layer_idx]):
            x = torch.relu(lin(x))
            if idx != self.num_heads - 1:
                x = self.dropout(x)
 
        # Attention
        # (batch_size, query_len, key_len) * (query_len, embed_dim, num_heads) -> (batch_size, query_len, num_heads)
        att_score = torch.matmul(x, x.transpose(-2, -1))  # [N, Lq, Nk] * [Nk, D, H] -> [N, Lq, H]
 
        if self.attn is None:
            self.attn = MultiHeadSelfAttention(embed_dim=self.embed_dim, num_heads=self.num_heads, dropout=self.dropout)
 
        # Attention weights (batch_size, query_len, num_heads)
        att_weights = self.attn(att_score).transpose(-2, -1)  # [N, Lq, H] * [H, Nk, D] -> [N, Lq, Nk]
        return att_weights


class PositionwiseFeedforward(torch.nn.Module):
    def __init__(self, d_in, d_hid, dropout):
        super().__init__()
        self.w_1 = torch.nn.Linear(d_in, d_hid)  # Linear layer to match the dimension of the input and hidden state in the feedforward layer
        self.relu = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(p=dropout)
        self.w_2 = torch.nn.Linear(d_hid, d_in)  # Linear layer to match the dimension of the hidden state and output tensor in the feedforward layer
 
    def forward(self, x):
        intermediate = self.w_1(x)  # Linear transformation
        intermediate = self.relu(intermediate)
        intermediate = self.dropout(intermediate)
        return self.w_2(intermediate)  # Linear transformation


class EncoderLayer(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout):
        super().__init__()
        self.self_attn = SelfAttention(embed_dim=embed_dim, num_heads=num_heads, dropout=dropout)
        self.feedforward = PositionwiseFeedforward(embed_dim=embed_dim, d_hid=2*embed_dim, dropout=dropout)
 
    def forward(self, x):
        # Self attention
        att_weights  = self.self_attn(x)  # [N, Lq, Nk]
        out1 = torch.matmul(att_weights, x)  # (batch_size, query_len, num_heads) * (query_len, embed_dim, num_heads) -> (batch_size, query_len, embed_dim)
 
        # Multi-head attention
        if att_weights.shape[-1] > 1:
            out2 = torch.mean(att_weights for a given feature map a single feature of interesting_interchange the model to build a new neural neural network from here to there is very simple but it has its own set of pitfating problems where the input and output are not in the same dimensionality. 
This was my first time using pytorch is a deep learning framework developed by FAIR which means fair software foundation, open-source, sustainable open-souce softwares with a non-zero cost to support their users. 

The next section will include information about how to build your own model from scratch for different purposes like object detection and image classification etc. The code for this repo will be available at https://github.com/deepaksh4392/pytorch_object_detection .


