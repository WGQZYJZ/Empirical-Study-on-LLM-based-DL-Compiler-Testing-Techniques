
class Attention(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.d_model = d_model
 
        self.qkv_projection  = torch.nn.Linear(in_features=self.d_model, out_features=3*self.d_model)
 
    def forward(self, query, key, value):
        output  = self._compute_attention_output(query, key, value)
        return output
 
    def _compute_attention_output(self, q, k, v):
        # Compute dot product of query and key tensors.
        qk  = torch.matmul(q, k.transpose(-2, -1))
 
        # Scale dot-product output by the inverse scale factor.
        scaled_qk  = self._scale_dot_product_output(qk)
 
        # Apply softmax over the last dimension of the scaled dot product.
        prob  = torch.nn.functional.softmax(scaled_qk, dim=-1)
 
        # Apply dropout to the softmax output and multiply it with value tensor to compute attention output.
        prob  = torch.nn.functional.dropout(prob, p=self._dropout_probability())
        return v @ prob
 
    def _scale_dot_product_output(self, qk):
        inv_scale_factor  = self.d_model ** -0.5
        return (qk / inv_scale_factor).div_(inv_scale_factor)
 
    def _dropout_probability(self):
        return dropout_p
