
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()

    def forward(self, x1, x2):
        # Get query & key
        qk = self.attn.proj_q @ self.attn.proj_k.transpose(-2, -1) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn.mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output

        # Get value
        v = self.attn.proj_v @ x2  # Compute the dot product of the query and value
        v = v + self.attn.mask  # Add the attention mask to the scaled dot product
        output = attn_weight @ v  # Compute the dot product of the dropout output and the value

        return output


# Initializing the model
m = Model()


