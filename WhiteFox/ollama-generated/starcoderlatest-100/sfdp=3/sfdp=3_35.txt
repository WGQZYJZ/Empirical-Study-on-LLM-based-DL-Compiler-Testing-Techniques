
class Attention(torch.nn.Module):
    def __init__(self, d_model: int):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_model)  # Project the input to a single dimension to obtain a single linear layer for the query
        self.key = torch.nn.Linear(d_model, d_model)  # Repeat the same operations for the key tensor
        self.value = torch.nn.Linear(d_model, d_model)  # Repeat the same operations for the value tensor
 
    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        nq, _ = q.shape
        nk, _ = k.shape
 
        query = self.query(q).view(nq, -1, 1) # Query shape should be (batch_size, d_model * num_heads, sequence_length)
        key = self.key(k).view(nk, -1, 1)
        value = self.value(v).view(nk, -1, 1)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) # Shape of query tensor is (batch_size, num_heads * d_model, sequence_length, sequence_length) and the shape of key tensor is (batch_size, num_heads * d_model, sequence_length, sequence_length). The dot product can be computed in this way.
        qk = qk.view(nq, nk, -1) # Shape of output tensor is (batch_size, num_heads * d_model, sequence_length * sequence_length)
 
        return qk
 
    def self_attention(self, x): # Here self-attention only need to be used in encoder and decoder
        x = self.query(x).view(-1, 8)
        attention = torch.matmul(x, x.transpose(0, -1)) * 0.75
        return attention
 
    def multihead_attention(self, x): # Here multi-head attention can be used in encoder and decoder
        nq, nk, _ = x.shape
        q = self.query(x).view(nq, -1, 8) # Shape of q tensor is (batch_size * num_heads, sequence_length, d_model / num_heads)
        k = self.key(x).view(nk, -1, 8)
        v = self.value(x).view(nk, -1, 8)
 
        attention = torch.matmul(q, k.transpose(-2, -1)) # Shape of output tensor is (batch_size * num_heads, sequence_length, sequence_length)
        attention *= 0.75
 
        scaled_attention = nn.functional.softmax(attention, dim=-1).mul(attention)
        softmax_attention = scaled_attention.view(nq, nk, -1) # Shape of output tensor is (batch_size * num_heads, sequence_length, sequence_length)
        return softmax_attention
 
    def relative_position_attention(self, x):
        b, l, _ = x.shape
 
        q = self.query(x).view(b, -1, 8) # Shape of q tensor is (batch_size * num_heads, sequence_length, d_model / num_heads)
        k = self.key(x).view(b, -1, 8)
 
        attention = torch.matmul(q, k.transpose(-2, -1)) * 0.75
        scaled_attention = nn.functional.softmax(attention, dim=-1).mul(attention) # Shape of output tensor is (batch_size * num_heads, sequence_length, sequence_length)
        softmax_attention = scaled_attention.view(b, l, -1) # Shape of output tensor is (batch_size * num_heads, sequence_length, sequence_length)
 
        return softmax_attention
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        d_model = 64 # Model dimension
 
        self.encoder = Encoder(d_model=d_model)
        self.decoder = Decoder(d_model=d_model, max_pos_encoding_scale=128)
        self.attention = Attention(d_model=d_model)
 
    def forward(self, x): # Here the output of encoder and decoder should be concatenated
        e = self.encoder(x) # Shape of encoder output tensor is (batch_size * num_heads, sequence_length, sequence_length, d_model / num_heads). The batch size is 1 because we only have one example in each batch.
        d = self.decoder(e) # Shape of decoder output tensor is (batch_size * num_heads, sequence_length, sequence_length, d_model / num_heads).
 
        attention = self.attention(d, e, e) # Shape of output tensor is (1, 59, sequence_length, sequence_length).
        output = torch.nn.functional.layer_norm(e + d * attention)
        return output


class Encoder(torch.nn.Module):
    def __init__(self, d_model: int):
        super().__init__()
 
        self.embedding = nn.Linear(d_model, 256) # Apply the linear layer to the input tensor to obtain a representation of sequence positions in dimension 102473757
        x:3 - Use - End
   59:8 - 59
