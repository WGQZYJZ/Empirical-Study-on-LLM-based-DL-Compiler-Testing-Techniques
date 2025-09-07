
class Query(torch.nn.Module):
    def __init__(self, input_dim=768, hidden_dim=3072):
        super().__init__()
        self.q_net = torch.nn.Sequential(
            torch.nn.Linear(input_dim, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, input_dim)
        )
 
    def forward(self, x1):
        qk = self.q_net(x1)  # Output from the linear layer
        return qk


class Key(torch.nn.Module):
    def __init__(self, input_dim=768, hidden_dim=3072):
        super().__init__()
        self.k_net = torch.nn.Sequential(
            torch.nn.Linear(input_dim, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, input_dim)
        )
 
    def forward(self, x2):
        qk = self.k_net(x2)  # Output from the linear layer
        return qk


class Value(torch.nn.Module):
    def __init__(self, input_dim=768, hidden_dim=3072):
        super().__init__()
        self.v_net = torch.nn.Sequential(
            torch.nn.Linear(input_dim, hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_dim, input_dim)
        )
 
    def forward(self, x3):
        qk = self.v_net(x3)  # Output from the linear layer
        return qk


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, head_dim=768, input_dim=768):
        super().__init__()
        self.head_dim = head_dim
        assert (input_dim % self.head_dim) == 0
 
        # The number of attention heads.
        self.num_heads = int(input_dim / self.head_dim)
        print('Number of attention heads: {}'.format(self.num_heads))
 
    def forward(self, query, key, value):
        qk = torch.cat([query, key], dim=-1)  # Concatenate the output from the two layers.
        # qk = (n, m, input_dim) -> (n, num_heads, input_dim / num_heads)
        qk = qk.view(-1, self.num_heads, self.head_dim).permute(0, 2, 1)
 
        attn_weights = torch.matmul(qk, key.transpose(-2, -1)) # Matrix multiplication of the scaled dot product and the transpose of the scaled dot product
        # attn_weights = (n, num_heads, input_dim / num_heads) @ (input_dim/num_heads, input_dim/num_heads) -> (n, num_heads, input_dim / num_heads)
        attn_weights = self._softmax(attn_weights, dim=-1) # Apply the softmax to the scaled dot product.
 
        output = torch.matmul(attn_weights, value)  # Matrix multiplication of the attention weights and the values.
        # output = (n, num_heads, input_dim / num_heads) @ (input_dim/num_heads, input_dim) -> (n, input_dim)
 
        return output

    def _softmax(self, attn_weights, dim=-1):
        softmaxed_attn_weights = torch.softmax(attn_weights, dim=dim) # Apply the softmax function to the scaled dot product

        # Make sure sum of each row is 1 before normalization
        assert torch.isclose(torch.sum(softmaxed_attn_weights, dim=-1), 1) # TODO: Replace this assertion with something smarter
 
        return softmaxed_attn_weights

class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = MultiHeadAttention()
 
    def forward(self, x3, x1):  # The query tensor is the last dimension in the model.
        # Query: (B, F, L), Key: (B, T, D), Value: (B, T, D)
        qk = self.attn(x3, x1, x1)
 
        return qk

class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = Query()  # Compute the dot product of a query tensor and a key tensor. The result is multiplied by the value tensor to get the output.
        self.key = Key()
        self.value = Value()
 
    def forward(self, x3, x1):
        qk = self.query(x3)  # The query tensor in the SelfAttention layer and the key tensor in the MultiHeadAttention layer are identical because we concatenate their outputs in the forward method of this class.
        v1 = self.attn(xk, x2, x1)  # The attention weight is used to compute a weighted sum of the value tensor.
 
        return v1
# Inputs to the model
x3 = torch.randn(2, 768, 64)
x1 = torch.randn(2, 768, 64)
