This pattern characterizes scenarios where an attention mechanism is applied to a query tensor, a key tensor and a value tensor. The `scale_factor` parameter represents the inverse scale factor that will be used for softmax, and can also represent the product of two other parameters in the implementation (see below).

 # Parameters
*   **query**: *(required)* A query tensor. Should have shape (batch size, input sequence length, hidden dimensions)
*   **key**: *(required)* A key tensor. Should have shape (batch size, output sequence length, hidden dimensions)
*   **value**: *(required)* A value tensor. Should have shape (batch size, output sequence length, hidden dimensions)
*   **scale_factor**: *(optional, default 1)* The scale factor used to scale softmax before computing the dot product of the query and key tensors

 # Model
class TransformerBlock(torch.nn.Module):
    def __init__(self, input_hidden_dim, output_hidden_dim):
        super().__init__()
        self.attention = Attention(...)

    def forward(self, x1):
        ...
     # Initializing the model
     b = TransformerBlock(... )

     # Inputs to the model
     i = torch.randn(batch size, input sequence length, input hidden dimensions)
     f = torch.randn(batch size, output sequence length, input hidden dimensions)
     h = torch.randn(batch size, output sequence length, output hidden dimension)
     o = torch.randn(batch size, output sequence length, output hidden dimension)

     # Output of the model
     attention_weights = b(i, f, g, scale_factor=1/np.sqrt(256))
