
class Transformer(torch.nn.Module):
    def __init__(self, nhead=8, d_k=64, nlayer=6):
        super().__init__()
        self.encoder = torch.nn.TransformerEncoderLayer(d_model=d_k * 32, num_heads=nhead)
 
    def forward(self, query, key, value):
        q = self.encoder(query, src_key_padding_mask=None, layer_id=-1)[0] # (bs, qlen, d_model)
        k = self.encoder(key, src_key_padding_mask=None, layer_id=-1)[0] # (bs, klen, d_model)
        v = self.encoder(value, src_key_padding_mask=None, layer_id=-1)[0] # (bs, vlen, d_model)
        output = torch.matmul(q, k.transpose(-2, -1)) * scale  # Compute the dot product of query and key tensors
        scaled_output = output.mul(scale_factor) # Scale the dot product by a factor
        softmax_output = scaled_output.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_output = torch.nn.functional.dropout(softmax_output, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_output.matmul(v) # Compute the dot product of the dropout output and the value tensor 
        return output


# Initializing the model
m = Transformer()

# Inputs to the model
x1 = torch.randn(batchsize, seq_length, dim).transpose(0, 1) 
