
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(10, 16, 4, 4), requires_grad=True)
        self.key   = torch.nn.Parameter(torch.randn(10, 8, 3, 3), requires_grad=True)
        self.value = torch.nn.Parameter(torch.randn(10, 256), requires_grad=False)

    def forward(self, x):
        # (batch, input_channel, sequence_len, input_seq_length) --> (batch * sequence_len, input_channel, input_seq_length)
        query = self.query @ self.key.transpose(-2, -1)  # Compute the dot product of query and key, and scale it
        attn_mask = torch.softmax(query, dim=-1)    # Apply softmax to the result
        qk     = attn_mask @ self.value          # Compute the dot product of the dropout output and the value
        attn_weight = torch.dropout(qk, dropout_p, True)  # Apply dropout to the softmax output

        return attn_weight @ x                  # Return the result


# Inputs to the model
x1 = torch.randn(2, 10, 16, 4)


