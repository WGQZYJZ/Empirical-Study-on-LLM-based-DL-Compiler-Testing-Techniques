
class Model(torch.nn.Module):
    def __init__(self, d_model, heads):
        super().__init__()
        self.d_model = d_model
        self.heads = heads
        self.scaling = 1 / math.sqrt(d_model)

    def forward(self, x1, x2, attn_mask):
        # Compute the scaled dot product of the input and the query
        # (see https://www.cs.toronto.edu/~hinton/absps/the- IllustratedAttention.pdf)
        v = torch.matmul(x1, x2) / self.scaling  # Shape: [batch_size, sequence_length, heads * d_model]

        # Compute the attention weights.
        qk = torch.einsum('bhcd,hbc->bcd', v, x2)  # Shape: [batch_size, sequence_length, heads * d_model]
        # Apply dropout to the output to keep only a fraction of the keys
        # and values for computing the attention weights.
        qk = torch.nn.functional.dropout(qk, p=0.5, training=self.training)

        # Scale the attention weights with a temperature factor for numerical stability.
        # Note that:
        # The softmax is calculated over all the elements of the tensor at once.
        # That is, each element has its own attention weight applied.
        # However, as in a linear transformation, this does not affect the shape
        # of the matrix.
        # Therefore, to calculate the mean value of the attention weights, we need
        # to divide each element by the square root of the d_model.
        qk *= self.scaling

        # Use attention mask to avoid performing attention on padding tokens.
        attn_weight = torch.softmax(qk, dim=-1)  # Shape: [batch_size, sequence_length, heads]

        # Multiply the input by the output of the softmax weights.
        # Shape: [batch_size, sequence_length, heads * d_model]
        x = torch.einsum('bhcd,hbc->bcd', attn_weight, v)  # Shape: [batch_size, sequence_length, heads * d_model]

        # Output projection layer. Scale the output with a temperature factor
        # for numerical stability to avoid exp() calls.
        x = torch.nn.functional.dropout(x / math.sqrt(self.d_model), p=0.5, training=self.training)

        return x

# Initializing the model
m = Model(8, 4)


