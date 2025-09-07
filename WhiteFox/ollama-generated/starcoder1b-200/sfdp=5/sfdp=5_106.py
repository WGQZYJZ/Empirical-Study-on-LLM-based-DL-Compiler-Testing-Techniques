
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.num_layers = num_layers
 
    def forward(self, x1):
        # Compute attn_weight using softmax.
        attn_weight = torch.softmax(
            x1  @ x2, dim=-1)  # x1 and x2 can be broadcast to shape (batch_size * sequence_length, hidden_size),
        # then attn_weight will be broadcast to shape (batch_size * sequence_length, hidden_size).

        # Compute output.
        value = x1  @ self.key  # Now value = x1  @ self.key
        # The value can be computed with shape (batch_size * sequence_length, hidden_size),
        # then the dropout operation is applied to the output by:
        # output = torch.dropout(output, p=self.dropout_p, training=self.training)

        # Add an extra dimension to value and reshape it back to original shape.
        attn_weight = attn_weight.view(-1, self.num_layers, 1)  @ value  # shape (batch_size * sequence_length, hidden_size),
        output = torch.dropout(attn_weight, p=self.dropout_p, training=self.training)

        return output


# Initializing the model
m = Model(num_layers)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
