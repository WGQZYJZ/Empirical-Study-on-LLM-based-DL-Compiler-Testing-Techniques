
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.Linear(768, 1024)

    def forward(self, query, key, attn_mask, value):
        qk = torch.einsum('bnchw,nbchw->bhnhw', (query, key)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.einsum('bhnhw,nbchw->bnchw', (attn_weight, value)) # Compute the dot product of the dropout output and the value

        return output


# Initializing the model
m2 = TransformerModel()

# Inputs to the model
x1  = torch.randn(2, 768, 512)
key = torch.randn(3, 1024, 128)
value = torch.randn(2, 1024, 128)
attn_mask = torch.randn(2, 3, 64, 64) # batch_size x n_head x input_seq_len x output_seq_len
__output2__ = m2(x1, key, attn_mask, value)

