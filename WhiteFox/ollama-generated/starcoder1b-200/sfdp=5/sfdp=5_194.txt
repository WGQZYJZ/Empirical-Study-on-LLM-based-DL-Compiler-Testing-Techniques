
class Model(torch.nn.Module):
    def __init__(self, qkv_size=32, attn_head=8, n_pos_emb=128, n_enc_layers=6):
        super().__init__()
        self.qkv  = torch.nn.Linear(n_pos_emb * 2 + 4 * qkv_size, 3 * qkv_size)
        self.attn_head = attn_head
        self.query = torch.nn.Linear(qkv_size + n_pos_emb, attn_head)
        self.value  = torch.nn.Linear(n_enc_layers * qkv_size, attn_head)
        self.dropout = nn.Dropout(p=0.5)

    def forward(self, x1, x2):
        n_batch, x1_dim, H, W = x1.size()

        # The encoder computes the initial embedding from two inputs: `query` and `key`.
        # Then, they concatenate along the batch axis to create a new input of shape `(n_batch, n_enc_layers * qkv_size)`,
        # which is required for feed-forward computing.
        x = torch.cat([x1, x2], dim=-1)
        key = self.query(x).contiguous()
        value  = self.value(self.dropout(torch.matmul(key, x)))

        # The output of the encoder is a new input to compute the logits (also called softmax scores).
        # The shape of these scores is `(n_batch, n_enc_layers * qkv_size, vocabulary)`.
        # To compute the attention weights, they are multiplied by `query` and added with an attention mask.
        key = key.view(n_batch, -1, self.attn_head, self.attn_head)
        attn  = torch.bmm(key, value)
        attn  = attn.contiguous().view(n_batch, -1, H, W)

        # This new input to compute the logits can be multiplied by a scale factor that depends on the position of the input tensor.
        # The shape of these scores is `(n_batch, vocabulary)`.
        x = torch.bmm(value, key) * math.sqrt(x1_dim)

        return x


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(1, 4, 256, 256).float().requires_grad_()
key   = torch.randn(1, 4, 256, 256).float().requires_grad_()
value  = torch.randn(1, 4, 256, 256).float().requires_grad_()
