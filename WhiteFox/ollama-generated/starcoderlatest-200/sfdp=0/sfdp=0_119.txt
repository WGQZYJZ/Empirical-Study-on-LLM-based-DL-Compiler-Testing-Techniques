
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.scale = torch.sqrt(float(dim))
 
    def forward(self, q, k, v):
        batch_size, head_num, seq_len, _ = q.shape

        # Split the query tensor into a set of vectors by using the same key tensor as the last dimension
        k = k.repeat(head_num, 1, 1, 1)
 
        # Dot-product between the query tensor and all keys in a batch to generate a single vector for each example
        dot_product = torch.matmul(q, k.transpose(-2, -1)) / self.scale
 
        # Softmax of the dot product values is computed as a probability distribution
        attention_weights = torch.softmax(dot_product, dim=-1)
 
        # Attention weights are used to compute the weighted sum of the value tensor in a batch
        attention_output = torch.matmul(attention_weights, v)
        return attention_output
 
class MultiHeadAttentionWithPositionEmbeddings(MultiHeadAttention):
    def forward(self, q, k, v, pos_emb):
        # Add position embedding to both the query and key tensors before computing their dot-product with other keys
        scaled_pos_emb = pos_emb.repeat(q.shape[0], self.head_num, 1)
        q += scaled_pos_emb
        k += scaled_pos_emb
 
        return MultiHeadAttention.forward(self, q, k, v)
 
class TransformerEncoderLayerWithEmbeddings(torch.nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward, dropout, activation, emb=None):
        super().__init__()
        self.norm1 = torch.nn.LayerNorm(d_model)
        self.attention = MultiHeadAttentionWithPositionEmbeddings(nhead, dim_feedforward)
        self.dropout = torch.nn.Dropout(p=dropout)
        self.norm2 = torch.nn.LayerNorm(d_model)
        self.ff = torch.nn.Linear(dim_feedforward, d_model * 4)
 
        if emb is not None:
            # Feed-forward layer for input embeddings with position embedding to account for the shift of each token in the batch
            self.positionwise = torch.nn.Sequential(
                torch.nn.LayerNorm(d_model),
                torch.nn.Linear(emb.shape[1] + d_model, dim_feedforward),
                activation(),
                torch.nn.Dropout(dropout)
            )
 
class TransformerEncoderWithEmbeddings(torch.nn.Module):
    def __init__(self, nlayers, d_model, nhead, dim_feedforward, dropout, activation, emb=None):
        super().__init__()
        self.embed = emb
 
        if emb is not None:
            # Feed-forward layer for input embeddings with position embedding to account for the shift of each token in the batch
            self.positional_embedding = torch.nn.Parameter(
                self._generate_position_encoding(emb), requires_grad=False)
        else:
            self.positional_embedding = None
 
        self.layers = torch.nn.ModuleList([
            TransformerEncoderLayerWithEmbeddings(
                d_model, nhead, dim_feedforward, dropout, activation, emb) for _ in range(nlayers)])
 
    def forward(self, src):
        # Embedding layer: the tokens are converted into vectors of `d_model` dimension and concatenated with an optional positional encoding tensor to get the final embedded vectors for each example.
        if self.emb is not None:
            batch_size = src.shape[0]
            src = torch.cat([src, self.positional_embedding[:, :batch_size, :]], dim=-1)
 
            # The attention mask needs to be converted into the same type as the embeddings for this model
            mask = src.new_zeros(batch_size, src.shape[-1]).byte()
 
        else:
            # Embedding layer is not required if input embeddings are specified in advance. They will always be used.
            mask = None
 
        for layer in self.layers:
            # Self-attention
            out = layer.attention(
                query=src,
                key=self.embed,
                value=self.embed,
                pos_emb=self.positional_embedding if self.positional_embedding is not None else None
            )
            src = out + src
 
            # Residual connection and dropout are performed here in case a new set of positional embeddings are to be learned or for the case that no new embeddings but some shifted version of already embedded vectors is used instead of the full input embeddings
            src2 = out + self.dropout(src)
            src = activation()(self.norm1(src2))
 
        return src
 
    @staticmethod
    def _generate_position_encoding(emb):
        # If an embedding tensor is specified for this model, a positional encoding layer will be used to shift each position of the embedded tokens by the corresponding offsets that are calculated according to this formula:
        # pos_emb[i] = sin(pos_enc_1 * (pos_i / dim_model)) * cos(pos_enc_2 * (pos_i / dim_model)
        if emb.shape[1] == 1:
            pos_enc_1 = emb[:, 0, :].unsqueeze(-2).unsqueeze(-3)
            pos_enc_2 = emb[:, :, 0, :].unsqueeze(-2).unsqueeze(-3)
        elif emb.shape[2] == 1:
            pos_enc_1 = emb[:, :, 0, :] * (emb[:, :, :, 0, :].unsqueeze(0)) ** (
                np.arange(2, emb emb:
       
defclass Test (E, 9), with model= (L, 23489, 5116, 7632, 422, 3563, 2327, 2041, 564, 2290, 3580),
# Input:
#    E.L.L. 2041 - 0.2234 5340 0.1513 4466 3769 0.1057 5057
#   [0.0051 -0.3089] [-0.3136] [0.4008 -2.5040] [-0.4559]]
#   [10.3887 7.1928] [10.1606 7.1689] [12.2678 7.8779] [0.7797 -0.4503]
#   3849.9409
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   0
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#   alpha: [[1 0]]
#   beta: [[0 0]]
#   6.7891689
#   10
#   x: [[ 1.00000000e+00 +1.00000000e-02]] # [1,0] (one row vector)
#   y: [ -0.4503 ]
#  000E-Fuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuseuse