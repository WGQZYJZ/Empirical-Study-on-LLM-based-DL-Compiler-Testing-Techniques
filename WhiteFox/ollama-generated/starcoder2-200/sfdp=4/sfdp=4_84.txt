
class MultiheadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # Compute the dot product of query and key, then scale it by the sqrt of the dimensionality of the key vector
        self.qk = torch.nn.Linear(d_k, d_k)
        self.v  = torch.nn.Linear(d_k, n_head * d_k)
 
        # Define the mask used in the scaled dot-product attention mechanism
        self._attn_mask = torch.zeros((1, maxlen, maxlen)).type('torch.FloatTensor')
        self._attn_mask[:, -maxlen:, :]  = -math.inf  # Past tokens don't attend to the current position (padding)
        self._attn_mask[:, :, :maxlen]  = -math.inf  # The current token doesn't attend to future tokens (padding).
 
        # Use softmax to compute the attention weights of the scaled dot-product attention mechanism
        self._softmax = torch.nn.Softmax(dim=-1)

    def forward(self, query):

        # Compute the dot product of query and key
        qk  = self.qk(query) 
       
        # Scale by sqrt of dimensionality of key vector
        scaled_attn_weights = math.sqrt(d_k * 1.)
        attn_weight  = self._softmax(scaled_attn_weights @ (qk  + self._attn_mask))

        v  = torch.nn.Linear(d_k, d_model)

        # Compute the weighted sum of the value vector 
        output  = torch.sum((v(query) * attn_weight), dim=1)
 
        return output


# Inputs to the model
maxlen = 300  # Maximum length of the sequence in the batch of input data
input_tensor  = torch.ones(8, maxlen + 2)
 
# Initialize the model
m = MultiheadAttention()

 
__output__  = m(input_tensor)

