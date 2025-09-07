
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k1, v1, scale=None, dropout_p=0.5):

        if scale is not None:
            inv_scale = torch.rsqrt(scale)
            scaled_qk  = qk * inv_scale
            softmax_qk  = scaled_qk.softmax(dim=-1)
            output = torch.nn.functional.dropout(softmax_qk, p=dropout_p).matmul(v1)
        else:
            scaled_qk  = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(k1.size(-1)) # scaling the dot product
            softmax_qk  = scaled_qk.softmax(dim=-1)  # Applying the softmax function to the output of the scaled dot product
            dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # applying dropout on the above result and multiply it with value
            output  = dropout_qk.matmul(v1)

        return output

# Initializing the model
m  = Model()

# Inputs to the model:
# query tensor shape (4x20) ,  key tensor shape (3x50),  value tensor shape (3x100). You may also pass None for the scale parameter.
q, k, v = torch.randn(4, 20), torch.randn(3, 50), torch.randn(3, 100)

 # Outputs from the model:
__output___ = m(__input__)

# Task 8.3.2: Use the following inputs/outputs to pass to the 'score_model_with_inputs' function for automated testing:
__input__, 