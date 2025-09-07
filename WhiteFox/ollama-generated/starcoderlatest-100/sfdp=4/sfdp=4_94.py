
class Attention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        # the first dimension of the linear layers below will be multiplied by `num_heads`
        self.query_lin = torch.nn.Linear(d_model, 32)
        self.key_lin = torch.nn.Linear(d_model, 32)
        self.value_lin = torch.nn.Linear(d_model, 32)

        # the output dimension of each linear layer is multiplied by `num_heads`
        self.attn_out = torch.nn.Linear(num_heads * d_k, d_model)
 
    def forward(self, q, k, v, attn_mask):
        batch_size = q.shape[0]
        # The first dimension of the result is multiplied by `num_heads` to create a new dimension in attention scores
        batched_q = torch.reshape(q, (batch_size, 1, -1)).repeat((self.num_heads, 1, 1))

        # Apply linear layers and convert queries, keys, and values to `num_heads` dimensions
        q = self.query_lin(batched_q).permute([0, 2, 1])
        k = self.key_lin(k).permute([0, 2, 1])
        v = self.value_lin(v)

        # The result will be of the form `num_heads` x `seq_len` x `d_model / num_heads`, where `attn_weight` is softmax of the scaled dot-product attention of `q` and `k`.
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)

        # Add the attention mask to the scaled dot-product attention weights
        if attn_mask is not None:
            attn_weights += attn_mask * 100000.

        # Apply softmax in `dim=-1` and divide by square root of `d_k`. Then, multiply it with `v`, which is a tensor containing the values from the key-value pairs
        attn_weight = torch.softmax(attn_weights, dim=-1) / math.sqrt(self.d_k)
        batched_output = torch.matmul(attn_weight, v).permute([0, 2, 1])

        # The output will be of the form `num_heads` x `seq_len` x `d_model / num_heads`. Then, convert it back to `seq_len` x `num_heads`
        attn_out = self.attn_out(batched_output)
        return torch.reshape(attn_out, (batch_size, -1, self.d_k))
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        d_model = 256
        num_heads = 4

        attn = Attention(d_model, num_heads)
        mlp = torch.nn.Sequential(
            torch.nn.Linear(attn.out_dim(), d_model),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(d_model, d_model),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
        )

        self.attention = attn
        self.mlp = mlp
 
    def forward(self, x):
        q = self.attention(x)
        return self.mlp(q)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
