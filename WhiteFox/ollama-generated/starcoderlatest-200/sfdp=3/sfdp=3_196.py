
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(128)
 
    def forward(self, qk, key, value, scale_factor, dropout_p=0.5):
        v  # Apply layer normalization to the query tensor
        attention_output = (qk * dropout_p + self.layer_norm(qk)).transpose(-2, -1) # Compute the output of dot product followed by an addition operator followed by a transpose operation with axis set to -2
        softmax_attention_output  = softmax_function(attention_output)  # Apply softmax function on attention_output
        scaled_attention_output = scaled_softmax_attention_output * dropout_p + v # Scale softmax output by dropout probability followed by an addition operator followed by a multiplication operator with a scalar of dropout_p followed by a subtraction operator followed by a multiplication operator with a scalar of scale_factor followed by an addition operator with the same scalar as before
        return scaled_attention_output


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(128, 3072)
key = torch.randn(128, 3072)
value = torch.randn(128, 128, 3, 64, 64)
scale_factor = torch.rand([])
dropout_p = torch.rand([])
